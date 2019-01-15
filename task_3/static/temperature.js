$(function() {
    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var sock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/temperature/");
    sock.onmessage = function(message) {
        var data = JSON.parse(message.data);
        var values = $("#values")
        var ele = $('<tr></tr>')

        ele.append(
            $("<td></td>").text(data.value)
        )

        values.append(ele)
    };
});