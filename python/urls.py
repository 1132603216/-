"""python URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import url
from django.urls import path

from python import view

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/', view.login),
    path('reg/', view.reg),         # 注册

    path('info/', view.info),       # 获取个人信息
    path('upload/', view.upload),   # 文件上传
    path('update/', view.update),   # 修改个人信息
    path('addFriend/', view.add_friend),    # 添加好友
    path('delFriend/', view.del_friend),    # 删除好友
    path('post/', view.psot_),    # 发布帖子
    path('stay/', view.stay),    # 留言

    path('getStay/', view.get_stay),    # 查看你指定帖子留言
    path('search/', view.search),    # 全文搜索
    path('getFriend/', view.all_friend),    # 获取所有好友
    path('allContent/', view.all_content),    # 获取所有基础病内容
    path('allSpeek/', view.all_speek),    # 获取所有帖子
    path('getSpeek/', view.get_speek),    # 查看指定帖子

    url('^$|index.html', view.index),
    url('login.html', view.login_htlml),
    url('stay.html', view.stay_html),
    url('person.html', view.person_html),
]


