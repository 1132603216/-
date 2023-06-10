
var head = $("header .header img")
const input = $("input[type='file']")
var friendContainer = $(".friends")

var userinfo = {}

// 个人中心初始化
function init() {
    $.ajax({
        url: HOST + "info/",
        type: 'post',
        headers: {
            'AUTHORIZATION': "jwt " + localStorage.token
        },
        success(data) {
            if (data) {   // 判断是否请求成功
                userinfo = data
                // 设置头像
                $(".header img").attr("src", `${HOST}static/img/${userinfo['head']}`)
                // 设置基本信息
                var v = $(".info-person .value")
                v[0].innerText = userinfo['nick']
                v[1].innerText = userinfo['sex'] == 1 ? "男" : "女"
                v[2].innerText = userinfo['username']
                getFriend(userinfo['id'])
            }
        }
    });
}

init()


input.change(function (e) {
    var formData = new FormData();//必须是new FormData后台才能接收到
    formData.append("contentid", "1")
    formData.append("contenttype", "1")
    formData.append("file", e.target.files[0]);
    $.ajax({
        url: HOST + "upload/",
        headers: {
            'AUTHORIZATION': "jwt " + localStorage.token
        },
        data: formData,
        type: 'post',
        datatype: "json",
        contentType: false, //必须false才会自动加上正确的Content-Type
        processData: false, //必须false才会避开jQuery对 formdata 的默认处理，XMLHttpRequest 会对 formdata 进行正确的处理 
        success: function (data) {
            if (data.status) {
                head.attr("src", `${HOST}static/img/${data.img}`)
                alert("头像更换成功！")
            } else if (data.error) {
                alert(data.error)
                return
            } else {
                alert("更新头像失败")
            }
        },
        error() {
            alert("更新头像失败")
        }
    });
})


function updatePw() {
    var p1 = prompt("新密码")
    if (p1.length < 6) return alert("密码长度需要大于6")
    var p2 = prompt("确认密码")
    if (p1 === p2) {
        $.ajax({
            url: HOST + "update/",
            type: 'post',
            headers: {
                'AUTHORIZATION': "jwt " + localStorage.token
            },
            data: {
                password: p1,
            },
            success(data) {
                if (data.status) alert("密码修改成功")
            },
            error() {
                alert("密码修改失败")
            }
        });
    } else {
        alert("密码不一致")
    }
}

function updateInfo(e) {
    var v = $(".person .info-person div .value")
    var u = $(".person .info-person div .update")
    var nick = ""
    var sex = ""
    if (e.innerText === "修改基本信息") {
        e.innerText = "保存"
        v.attr("hidden", true)
        u.attr("hidden", false)
        nick = v[0].innerText
        sex = v[1].innerText === "男" ? 1 : 0
        u[0].value = nick
        u[1].value = sex
    } else {
        e.innerText = "修改基本信息"
        // 如果都相等不用发送修改请求
        if (u[0].value === nick || u[1].value === sex)
            return
        v[0].innerText = u[0].value
        v[1].innerText = u[1].value == 1 ? "男" : '女'

        u.attr("hidden", true)
        v.attr("hidden", false)

        $.ajax({
            url: HOST + "update/",
            type: 'post',
            headers: {
                'AUTHORIZATION': "jwt " + localStorage.token
            },
            data: {
                nick: u[0].value,
                sex: parseInt(u[1].value),
            }
        });
    }
}


// 获取所有好友
function getFriend(id) {
    $.ajax({
        url: HOST + "getFriend/",
        type: 'post',
        headers: {
            'AUTHORIZATION': "jwt " + localStorage.token
        },
        data: {
            id
        },
        success(data) {
            for (user of data) {
                // 设置好友信息
                var friend = $(`<div class='friend'></div>`)
                var u = $(`
                    <div class="user">
                        <img src="static/img/${user.head}" alt="">
                        <span class="username">${user.nick}</span>
                    </div>
                `)
                var b = $(`<button class="del">删除</button>`)
                var hr = $("<hr/>")
                
                b.click(delClick(user.username,friend,hr))
                friend.append(u).append(b)
                friendContainer.append(friend).append(hr)
            }
        }
    })
}

function delClick(username,dom,hr){
    return delFriend.bind(this,username,dom,hr)
}


function delFriend(username,dom,hr) {
    if(!confirm("确认删除这个好友吗")) return   // 删除好友
    $.ajax({
        url: HOST + "delFriend/",
        type: 'post',
        headers: {
            'AUTHORIZATION': "jwt " + localStorage.token
        },
        data: {
            username
        },
        success(data) {
            if(data.status){
                // getFriend()
                dom.remove()
                hr.remove()
            }
        }
    })
}

// 添加好友
function addFriend(){
    var username = prompt("好友账号")
    $.ajax({
        url: HOST + "addFriend/",
        type: 'post',
        headers: {
            'AUTHORIZATION': "jwt " + localStorage.token
        },
        data: {
            username
        },
        success(data) {
            if(data.msg){
                alert(data.msg)
                if(data.status) location.reload();
            }else{
                alert("添加失败")
            }
        }
    })

}

// 发布帖子
function post(e){
    $.ajax({
        url: HOST + "post/",
        type: 'post',
        headers: {
            'AUTHORIZATION': "jwt " + localStorage.token
        },
        data: {
            id:userinfo['id'],
            contents: $(".post textarea").val().trim()
        },
        success(data) {
            if(data.status){
                alert("发帖成功")
                location.reload()
            }
        }
    })
}