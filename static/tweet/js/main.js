$(function () {

//
// var tweets=$('#listtweet');
// tweets.each(function (index,element) {
//
// });
$(".tweetlist").click(function(){
    var url = $(this).find('#tweetdetial').attr('href');
    console.log (url);
    location.href = url

});
//
//
// $(".tweetdetial").click(function(){
//     var url = $(this).attr()
//     console.log (url);
//     // location.href = "detail-tweet"
//
// });


});