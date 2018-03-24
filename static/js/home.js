



$(document).ready(function () {
    $('.tabs').tabs();
    $('.modal').modal();
     $('.modal2').modal();
    //  $('#modal').modal('type','id');
    $('select').formSelect();

    $('.datepicker').datepicker({
        format:'dd/mm/yyyy',
        parse:null,
        firstDay:0,
        // minDate:Date.now(),
        // minDate:today.getDate(),
        // minDate:new Date(),
        maxDate:null});
        updateTabContent(-1);


});
 // function click5(type,id)
 // {
 //     $('.modal2').modal('open');
 //     var getid = document.getElementById('id').value;
 //     var gettype = document.getElementById('type').value;
 //
 //
 // }
function updateTabContent(type)
{
    alert(type);
    if(type===-1)
    {

        alert("Insideee -1 1st Methoddddd")
         var gettoken = document.getElementById('token').value;
        // json={"Type":-1,"Encoded":token};
        c=getJson(type,gettoken);
         callAPI(c);

    }

    else if(type===0)
    {

        alert("Insideee 0 2nd Methoddddd")
         var gettoken = document.getElementById('token').value;
        // json={"Type":-1,"Encoded":token};
        c=getJson(type,gettoken);
         callAPI(c);

    }

    else
    {

        alert("Insideee 1 3rd Methoddddd")
         var gettoken = document.getElementById('token').value;
        // json={"Type":-1,"Encoded":token};
        c=getJson(type,gettoken);
         callAPI(c);

    }

}
function getJson(value,token) {
    alert("Inside Secondd Methoddd");
    return {"Type":value,"Encoded":token};

}
function callAPI(JSON) {
    alert("Callinggg APPIIIIIII");
    alert("JSONNNNNNN=",JSON);
    console.log(JSON);
    $.ajax({

        url: '/todo/display/',
        method: "GET",
        data: JSON,
        // dataType: 'application/json; charset=utf-8',
        success:function (html)
        {
            console.log(html);
            $('#tab_content').html(html);





            }

    });




}


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

