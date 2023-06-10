if (location.hash) {
    change()
}


function change() {
    if ($("h1").text() === "登录") {
        $("h1").text("注册")
        $('input[type="submit"]').val("注册")
        var pw2 = $(`
        <label for="password2">确认密码</label>
        <input id='ok' type="password" required>
        `)
        $("form input[type='submit']").before(pw2)
        $("label[for='username']").text("用户名")
        $("#change").text("登录")
    } else {
        $("#change").text("没有账户？点击注册")
        $("h1").text("登录")
        $("#ok").remove()
        $("label[for='username']").text("账号")
        $("label[for='password2']").remove()
        $('input[type="submit"]').val("登录")
    }
}


function login() {
    $.ajax({
        type: "POST",
        url: HOST+"login/",
        data,
        success: function (d) {
            if(d.token){
                localStorage.token = d.token
                location.href = "index.html"
            }else{
                alert("登录失败")
            }
        },
        error(){
            alert("登录失败")
        }
        
    });
}

function register(){
    $.ajax({
        type: "POST",
        url: HOST+"reg/",
        data,
        success (d) {
            if(d.token){
                alert("请保存好该账户，这是你用于登录的账号名： "+d.username)
                localStorage.token = d.token
                location.href = "index.html"
            }else{
                alert("注册失败")
            }
        },
        error(){
            alert("注册失败")
        }
    });
}

function submit_(e){
    data = {}
    data.username = $("input")[0].value.trim()
    data.password = $("input")[1].value.trim()
    if($("input[type='submit']").val() === "登录"){
        login(data)
    }else{
        if($("input")[2].value.trim() === data.password){
            if(data.password.length < 6){
                alert("密码过短, 至少输入6位")
            }else{
                register(data)
            }
        }else{
            alert("密码不一致")
        }
    }
    return false
}





