$(function () {


    $(".tweetlist").click(function () {
        var url = $(this).find('#tweetdetial').attr('href');
        console.log(url);
        location.href = url

    });


    $(".showmessage").click(function (e) {
        e.preventDefault();
        var url = $(this).attr('name');
        window.open(url, "myWindow", 'width=400,height=200');


        var url_to_change_isread = '/ajax/change_status/';
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
            success: function (data) {
                if (data.success) {
                    alert("ajax call success.");
                } else {
                    alert("ajax call not success.");
                }
            }
        });
    });

//
//     $('.showmessage').click(function (event) {
//         $('.bg-modal').css('display','flex');
//         // $('.bg-modal').css('display','flex');
//
//     });
//
//
//     $('.close').click(function (event) {
//         $('.bg-modal').css('display','none');
//     });


    // $("#button_id").on('click', function () {
    //     var username = $(this).val();
    //     var active =
    // <
    //     true > // or false, you have to set it
    //     var active =
    // <
    //     id > // you have to set it
    //     $.ajax({
    //         url: '/ajax/validate_username/',
    //         data: {
    //             'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
    //             'active': active
    //             'job_id': username
    //         },
    //         dataType: 'json',
    //         success: function (data) {
    //             if (data.success) {
    //                 alert("ajax call success.");
    //                 // here you update the HTML to change the active to innactive
    //             } else {
    //                 alert("ajax call not success.");
    //             }
    //         }
    //     });
    //
    // });

});