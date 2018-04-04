function showTodoList() {

    var gettoken = document.getElementById('token').value;
    $.ajax({

        url: '/todo/side/',
        method: "GET",
        data: {"Token":gettoken},
        success:function (response)
        {
            console.log("Inside new Ajaxxxxx");
            console.log(response);
            console.log("After getting Html in New ajax");
            $('#new_div').html(response);

        }

    });

}
$(function () {
   showTodoList();
});