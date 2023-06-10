import json
import re
from time import *

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import hashlib
from base.models import *
from django.db.models import Q
from .utils.jwt_auth import *


def index(request):
    return render(request, 'index.html')

def login_htlml(request):
    return render(request, 'login.html')

def stay_html(request):
    return render(request, 'stay.html')


def person_html(request):
    return render(request, 'person.html')


def login(request):
    if request.method != 'POST':
        return JsonResponse({})
    req = request.POST
    username = req.get("username")
    password = req.get("password")
    if username and password:
        if not User.objects.filter(username=username, password=password):
            return JsonResponse({})
        token = create_token({"username": username})
        print(token)
        return JsonResponse({'token': token}, json_dumps_params={"ensure_ascii": False})
    return JsonResponse({})


def reg(request):
    if request.method != 'POST':
        return JsonResponse({})
    req = request.POST
    username = req.get("username")
    password = req.get("password")
    if len(username) > 20 or len(password) > 20:
        return JsonResponse({"msg": "用户名或密码过长"})
    h = username + str(time())
    sha = hashlib.sha1(h.encode('utf-8'))
    sha = sha.hexdigest()[7:14]
    user = User(nick=username, password=password,username=sha)
    user.save()

    token = create_token({"username": sha})
    return JsonResponse({'token': token,'username':sha},
                        json_dumps_params={"ensure_ascii": False})


# 获取个人信息
def info(request):
    if request.method != 'POST':
        return JsonResponse({})
    # 获取用户信息
    user = User.objects.filter(username=request.userinfo['username'])
    # print(user.values())
    user = user.values()[0]

    del user['password']
    data = json.dumps(user)
    # data = serializers.serialize('json',user)
    return HttpResponse(data, content_type="application/json")


def upload(request):
    # 请求方法为POST时,进行处理;
    if request.method != "POST":
        return JsonResponse({})
    # 获取上传的文件,如果没有文件,则默认为None;
    file = request.FILES.get("file", None)
    if file is None:
        return JsonResponse({'error': '没有找到文件'})
    # 打开特定的文件进行二进制的写操作;
    suffix = ['.gif', '.webp', '.jpg', '.jpge', '.png']
    suffix_index = file.name.rfind(".")
    if suffix_index == -1:
        return JsonResponse({'error': '需要图片'})
    if file.name[suffix_index:] not in suffix:
        return JsonResponse({'error': '需要图片'})

    head = f'{time()}{file.name}'
    with open(f"./static/img/{head}", 'wb+') as f:
        for chunk in file.chunks():
            f.write(chunk)
    # 关联数据库
    user = User.objects.get(username=request.userinfo['username'])
    user.head = head
    user.save()
    return JsonResponse({'status': 1, "img": f"{head}"})


def update(request):
    if request.method != "POST":
        return JsonResponse({})
    password = request.POST.get("password")
    nick = request.POST.get("nick")
    sex = request.POST.get("sex")
    user = User.objects.get(username=request.userinfo['username'])
    if password:
        user.password = password
    elif nick and sex:
        user.nick = nick
        user.sex = sex == 1 if 1 else 0
    else:
        return JsonResponse({})
    user.save()
    return JsonResponse({"status": True})


"""
username: 好友账号
判断
    是否有该参数
    该用户是否存在
    该用户是否是自己
    是否有该好友

获取用户id和自己的id添加数据

username： 用户账号
"""

def add_friend(request):
    if request.method != "POST":
        return JsonResponse({})
    username = request.userinfo['username']
    friend_username = request.POST.get("username")

    my = User.objects.filter(username=username).values()[0]
    print(my)
    # 判断好友是否存在
    friend = User.objects.filter(username=friend_username).values()
    if not friend:
        return JsonResponse({"msg": "没有找到该好友"}, json_dumps_params={"ensure_ascii": False})

    # 判断是否有该好友
    print(friend[0])
    f = Friend.objects.filter(userid=my['id'],userid2=friend[0]['id'])
    # 如果有该好友则不添加
    if f:
        return JsonResponse({"msg":"已有该好友"},json_dumps_params={"ensure_ascii": False})

    Friend(userid=my['id'],userid2=friend[0]['id']).save()
    return JsonResponse({"status":True,"msg":"添加成功"},json_dumps_params={"ensure_ascii": False})




# username，好友账号
def del_friend(request):
    if request.method != "POST":
        return JsonResponse({})
    username = request.userinfo['username']
    friend_username = request.POST.get("username")
    print(friend_username)
    if not friend_username or username == friend_username:
        return JsonResponse({})

    user = User.objects.filter(username=username)
    friend = User.objects.filter(username=friend_username)
    Friend.objects.filter(userid=user[0].id, userid2=friend[0].id).delete()
    # pass
    return JsonResponse({"status": True})


# 内容, contents: 内容， id：用户id
def psot_(request):
    if request.method != "POST":
        return JsonResponse({})
    contents = request.POST.get("contents")
    id = request.POST.get("id")
    # int(id)
    if not contents:
        return JsonResponse({})
    # t = strftime("%Y-%m-%d %H:%M:%S",localtime(time()))
    Speak(userid=id, content=contents).save()
    return JsonResponse({"status": True})


"""
留言： 哪个帖子，哪个人发布的留言，内容，时间
contents: 留言内容
speekid: 帖子id
id: 自身的id
"""
def stay(request):
    if request.method != "POST":
        return JsonResponse({})
    contents = request.POST.get("contents")
    speekid = request.POST.get("speekid")
    id = request.POST.get("id")
    if not contents or not speekid or not id:
        return JsonResponse({})
    Remain(userid=id, speekid=speekid, remain=contents).save()
    return JsonResponse({"status": True})


"""
全部朋友
id： 自身id
"""
def all_friend(request):
    if request.method != "POST":
        return JsonResponse({})
    id = request.POST.get("id")
    if not id:
        return JsonResponse({})
    friend = Friend.objects.filter(userid=id)
    users = []
    for f in list(friend.values_list()):
        user = User.objects.filter(id=f[2]).values()[0]
        del user['password']
        users.append(user)

    json_data = json.dumps(users)
    return HttpResponse(json_data, content_type="application/json")


# 全部内容
def all_content(request):
    contents = Contents.objects.filter().values()
    data = []
    for content in contents:
        data.append(content)
    data = json.dumps(data)
    # data = serializers.serialize("json",contents)
    return HttpResponse(data, content_type="application/json")


# 全部帖子
def all_speek(request):
    data = []
    for speak in Speak.objects.filter().values():
        speak['date'] = str(speak['date'])
        # 查询用户
        user = User.objects.filter(id=speak['userid']).values()[0]
        del user['password']
        user.update(speak)
        data.append(user)
        print(user)
    data = json.dumps(data)
    return HttpResponse(data, content_type="application/json")


# 全文搜索
# word
def search(request):
    if request.method != "POST":
        return JsonResponse({})
    words = request.POST.get("word",False)
    words = re.split(r' +',words)
    print(words)
    # q = NULL
    q = Q(content__contains=words[0]) | Q(title__contains=words[0]) | Q(type__contains=words[0])
    for word in words[1:]:
        q &= Q(content__contains=word) | Q(title__contains=word) | Q(type__contains=word)

    result = Contents.objects.filter(q).values()
    data = []
    for r in result:
        data.append(r)
    print(data)
    return JsonResponse({"status":True,"data":data})


# 需要把所有留言者找出，需要把留言本人找出
# 帖子id： id
def get_stay(request):
    id = request.GET.get("id",False)
    if not id:
        return JsonResponse({})
    remains = Remain.objects.filter(speekid=id).values()
    users = []
    for remain in remains:
        user = User.objects.filter(id=remain['userid']).values()[0]
        del user['password']
        user['remain'] = remain['remain']
        users.append(user)
    print(users)
    # print(remain)
    # 帖子id  所有留言者用户
    return JsonResponse({"status":True,'data':users})


def get_speek(request):
    id = request.GET.get("id",False)
    if not id:
        return JsonResponse({})
    speak = Speak.objects.filter(id=id).values()[0]
    print(speak)
    user = User.objects.filter(id=speak['userid']).values()[0]
    speak = {
        "head":user['head'],
        "nick": user['nick'],
        "content": speak['content'],
        "date":speak['date']
    }
    return JsonResponse({"status":True,'data':speak},json_dumps_params={"ensure_ascii": False})


