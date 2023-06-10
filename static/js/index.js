var userinfo = null
var main = $("main")
var body = $(`body`)

function setInfo() {
    // 需要登录
    $("#login").attr("id", "out").text("退出登录")
    $("#reg").hide()
    if (!userinfo.head) {
        userinfo.head = "default.webp"
    }
    $(".logo img").attr("src", HOST + 'static/img/' + userinfo.head)
}

// 是否能进个人中心、
function intoPerson() {
    if (!userinfo) return
    // 进入个人中心
    location.href = "person.html"
}

function login(e) {
    if (e.target.inerrText !== "登录") {
        localStorage.clear()
    }
}

if (localStorage.token) {
    $.ajax({
        type: "POST",
        headers: {
            'AUTHORIZATION': "jwt " + localStorage.token
        },
        url: HOST + "info/",
        success: function (data) {
            if (!data.error) {
                userinfo = data
                setInfo()
            }
        }
    });
}


// 帖子

function invitation() {
    $.ajax({
        type: "GET",
        url: HOST + "allSpeek/",
        success: function (data) {
            main.remove()
            main = $(`<main></main>`)
            for (speak of data) {
                var summary = $(`<div class="summary">
                    <div class="nick-container">
                    <img class="userhead" src="./static/img/${speak.head}" alt=" ">
                    <span class="nick">${speak.nick}</span>
                    </div>
                    <p>${speak.content}</p>
                    <hr>
                    <div class="comment">
                    <a href="stay.html?id=${speak.id}">看看其他人的留言吧</a>
                    <input type="text" placeholder="留言..">
                    <button class="button" onclick="send(this,${speak.id})">发送</button>
                    </div>
                    </div>`)
                main.append(summary)
            }
            body.append(main)
        }
    });

}

// 得到所有数据
$.ajax({
    type: "GET",
    url: HOST + "allContent/",
    success: function (d) {
        for (content of d) {
            var p_s = content.content.split("\n")
            var summary = $(`<div class="summary"><h2>${content.title}</h2></div>`)
            for (p of p_s) {
                summary.append($(`<p><span class="block"></span>${p}</p>`))
            }
            summary.append($(`<i>${content.type}</i>`))
            main.append(summary)
        }
    }
});


function send(e, speekid) {
    // 判断是否有权限访问
    if (!localStorage.token) return alert("请登录")
    var input = $(e).prev()
    var contents = input.val().trim()
    // console.log(ly);
    if (!contents) {
        alert("留言内容不能为空")
    }
    $.ajax({
        type: "POST",
        url: HOST + "stay/",
        headers: {
            'AUTHORIZATION': "jwt " + localStorage.token
        },
        data: {
            contents,
            speekid,
            id: userinfo.id
        },
        success(data) {
            if(data.status){
                alert("发送成功")
                input.val("")
            }
        }
    });
}

function search_() {
    word = $("#search").val().trim()
    if (!word) return false
    $.ajax({
        type: "POST",
        url: HOST + "search/",
        data: {
            word
        },
        success(data) {
            if (data.status) {
                data = data.data
                console.log(main);
                main.remove()
                main = $(`<main></main>`)
                for (content of data) {
                    console.log(content);
                    var p_s = content.content.split("\n")
                    var summary = $(`<div class="summary"><h2>${content.title}</h2></div>`)
                    for (p of p_s) {
                        summary.append($(`<p><span class="block"></span>${p}</p>`))
                    }
                    summary.append($(`<i>${content.type}</i>`))
                    main.append(summary)
                }
                body.append(main)
            }
        }
    });
    return false
}