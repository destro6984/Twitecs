$(function () {

// click on tweet -redirect to tweet deatil
    $(".tweetlist").click(function () {
        var url = $(this).find('#tweetdetial').attr('href');
        console.log(url);
        location.href = url

    });

// open unread message to new window ,change message to is_read-TRUE
    $(".showmessage").click(function (e) {
        e.preventDefault();
        var url = $(this).attr('name');
        window.open(url, "", 'width=700,height=200');

        $('#messnew').css('border-color', 'black');


        var url_to_change_isread = '/change_status/';
        pk = $(this).attr('id');
        $.ajax({
            type: "GET",
            url: url_to_change_isread,
            data: {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'is_read': true,
                'pk': pk,
            },
            dataType: 'json',
        });
    });
// open popup window to add new message
    $('#newtweet').click(function (e) {
        $('.bg-modal').css('display', 'flex')
    });

    $('.close').click(function () {
        $('.bg-modal').css('display', 'none')
    });
// shining messages
    if (($('#messagesbutton span').attr('id') == 'True')) {
        setInterval(function () {
            if ($('#messagesbutton span').attr('class') == 'bt-one') {
                $('#messagesbutton span').toggleClass('bt-one', 'bt-two');
            } else {
                $('#messagesbutton span').toggleClass('bt-two', 'bt-one');
            }

        }, 700);
    }
// display firest 30 chars in message
    $('#textmessage').each(function () {
        var shorttext=$(this).text().substr(1,50);
        $(this).text(shorttext);


    })


});
