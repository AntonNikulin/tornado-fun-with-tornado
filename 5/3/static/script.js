$(document).ready(function() {
    document.session = $('#session').val();
    $('#add-button').click(function(event) {
        requestInventory();
    });

    function requestInventory() {
        var val = $("#input").val();
        var host = 'ws://localhost:8000/counter';
        var ws = new WebSocket(host);
        ws.onopen = function (evt) { 
            console.log("conn open!")
            ws.send(val)

        };
        ws.onmessage = function(evt) {
            $('#status').append("<p style=\"color:green\">message "
                +evt.data+"</p>")
            $("#result").text(evt.data);
            console.log("message "+evt.data)
        };
        ws.onerror = function (evt) { };
    };
});
