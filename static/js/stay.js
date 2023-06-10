var speakid = location.search.split("?")[1].split("=")[1]
var userinfo = null
function getInfo() {
    $.ajax({
        type: "GET",
        url: HOST + "getSpeek/?id=" + speakid,
        success: function (data) {
            if (data.status) {
                userinfo = data.data
                setInfo()
            }

        }
    });
}


function setInfo() {
    var summary = $(`
            <div class="main summary">
            <div class="user">
                <img src="./static/img/${userinfo.head}" alt=" ">
                <span class="nick">${userinfo.nick}</span>
            </div>
            <hr>
            <p>${userinfo.content}</p>
                </div>
            `)
    $("main").prepend(summary)
}

getInfo()

$.ajax({
    type: "GET",
    url: HOST + `getStay/?id=${speakid}`,
    success: function (data) {
        if (data.status) {
            var comment = $(".comment")
            data = data.data
            console.log(data);
            for (d of data) {
                var summary = $(`
                            <div class="comment">
                                <div class="summary">
                                    <div class="user">
                                        <img src="./static/img/${d.head}" alt=" ">
                                        <span class="nick">${d.nick}</span>
                                    </div>
                                    <hr>
                                    <p>${d.remain}</p>
                                </div>
                            </div>
                            `)
                comment.append(summary)
            }
        }
    }
});
