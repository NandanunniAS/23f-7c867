var messages;
$("#fstatus").empty().append("online")
$("#messenger").submit(function(event) {
    $("#fstatus").empty().append("online")
    event.preventDefault();
    var $form = $(this),
        message = $form.find("input[name='message']").val(),
        url = $form.attr("action");
    if (message == "")
        message = "."
    $("#chatbox").append("<div class='me-msg'><div class='msg me-text-msg'>" + message + "</div></div>")
    $("input[name='message']").val('');
    $("#fstatus").empty().append("typing ...")
    $.post(url, { msg: message }).done(function(response) {
        $("#chatbox").append("<div class='ai-msg'><div class='msg ai-text-msg'>" + response.reply + "</div></div>")
        $("#fstatus").empty().append("offline")
    });
});