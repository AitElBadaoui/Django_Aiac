$("button#submit").click( function () {
$.post( $("#oublieMotPasseForm").attr("action"),
$("#oublieMotPasseForm :input").serializeArray(),function(data){
$("div#extentionForm").html(data);
});
$("#oublieMotPasseForm").submit(function (){
return false;
});
});

$("button#submit1").click( function () {
$.post( $("#loginForm").attr("action"),
$("#loginForm :input").serializeArray(),function(data){
$("div#warnmessage").html(data);
});
$("#loginForm").submit(function (){
return false;
});
});

