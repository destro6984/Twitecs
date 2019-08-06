$(function () {

// clicko on tweet -redirect to tweet deatil
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


        var url_to_change_isread = '/change_status/';
        pk=$(this).attr('id');
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
$('#newtweet').click(function(e) {
	$('.bg-modal').css('display', 'flex')
});

$('.close').click( function() {
	$('.bg-modal').css('display','none')
});


});