



$(document).ready(function () {
    $('.tabs').tabs();
    $('.modal').modal();
    $('select').formSelect();
    $('.datepicker').datepicker({
        format:'dd/mm/yyyy',
        parse:null,
        firstDay:0,
        // minDate:Date.now(),
        // minDate:today.getDate(),
        minDate:new Date(),
        maxDate:null});



});

function click4() {
    var gettitle = document.getElementById('title').value;
    var gettoken = document.getElementById('token').value;
    var getdesc = document.getElementById('desc').value;
    var getdate = document.getElementById('date').value;
    // var getselect = document.getElementById('select').value;



    alert(gettitle);
    // alert(getselect);
    alert(getdesc);
    alert(getdate);
    alert(gettoken);
    $.ajax({

        url: '/todo/home/',
        method: "POST",
        data: {"Title": gettitle,"Desc":getdesc,
            "Date":getdate,"Token":gettoken},
        // dataType: 'application/json; charset=utf-8',
        success:function (base)
        {
            console.log(base);
            alert(base);
            alert(base.Success);
            // token=check.Encoded;
            if(base.Success==true)
            {

                console.log("Insideeeee succcessss offf LLLooogginnn");
                // myemail=check.Email
                token=base.Token
                window.location.href="/todo/profile?Token="+token;
            }
            else
            {
                console.log("Innnnsiiiideee Faaalllseee of login  jssss");

                alert(base.Message);


                window.location.href="/todo/home";



            }
        }
    });
}

