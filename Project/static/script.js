
document.addEventListener('DOMContentLoaded', function() {
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    socket.on('connect', function() {
        console.log("Socket connected.");
        document.getElementById('startButton').onclick = function() {
            socket.emit('start_script');
            console.log('Start script emitted');
        };

        var inputButtons = document.querySelectorAll('.inputButton');
        inputButtons.forEach(button => {
            button.onclick = function() {
                console.log('Button clicked, sending input:', button.value);
                socket.emit('send_input', {data: button.value});
                console.log('Sent input:', button.value);  // This line is for debugging purposes.
            };
        });
    });

    socket.on('script_output', function(msg) {
        const output = document.getElementById('output');
        output.textContent += msg.data;
        output.scrollTop = output.scrollHeight; // Auto-scroll to bottom as new text is added.
    });
});