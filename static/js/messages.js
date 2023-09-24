
function loadMessages(receiverUsername) {
    $.ajax({
        url: "{% url 'get_messages' %}",
        data: { receiver_username: receiverUsername },
        dataType: "json",
        success: function (data) {
            if (data.messages) {
                // Update your message container to display messages
                // Example: You can append messages to a div with id "message-list"
                var messageList = $("#message-list");
                messageList.empty(); // Clear existing messages
                for (var i = 0; i < data.messages.length; i++) {
                    var message = data.messages[i];
                    messageList.append("<p><strong>" + message.sender + ":</strong> " + message.content + "</p>");
                }
            }
        },
        error: function (error) {
            console.error(error);
        },
    });
}

function sendMessage(receiverUsername, messageContent) {
    $.ajax({
        url: "{% url 'send_message' %}",
        type: "POST",
        data: {
            receiver_username: receiverUsername,
            message_content: messageContent,
            csrfmiddlewaretoken: "{{ csrf_token }}", // Include the CSRF token
        },
        dataType: "json",
        success: function (data) {
            if (data.success) {
                // Handle success (e.g., clear input field, update message list)
                $("#message-content").val(""); // Clear the message input
                loadMessages(receiverUsername); // Refresh message list
            } else {
                console.error("Message sending failed: " + data.error);
            }
        },
        error: function (error) {
            console.error(error);
        },
    });
}

$(document).ready(function () {
    // Example: Load messages for a specific receiver on page load
    var receiverUsername = "receiver_username_here";
    loadMessages(receiverUsername);

    // Example: Handle form submission to send a message
    $("#message-form").submit(function (event) {
        event.preventDefault();
        var messageContent = $("#message-content").val();
        sendMessage(receiverUsername, messageContent);
    });
});

