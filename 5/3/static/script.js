$(document).ready(function() {
    document.session = $('#session').val();
    $('#add-button').click(function(event) {
        requestInventory();
    });

    function requestInventory() {
        var host = 'ws://localhost:8000/counter';
        var ws = new WebSocket(host);
        ws.onopen = function (evt) {             
            $('#status').append("<p>add pressed</p>")
            console.log("conn open!")
            ws.send("Hi")

        };
        ws.onmessage = function(evt) {
            $('#status').append("<p style=\"color:green\">message "+evt.data+"</p>")
            console.log("message "+evt.data)
        };
        ws.onerror = function (evt) { };
    };
});
