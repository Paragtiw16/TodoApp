var flag_home_notification;
var count_overdues;
var count_dues;

$(document).ready(function () {
    $('.tabs').tabs();
    $('.modal').modal();
    $('.sidenav').sidenav();


    //  $('#modal').modal('type','id');
    $('select').formSelect();
    $('.datepicker').datepicker({

        //  onOpen: function() {
        //   $('.datepicker-modal').appendTo('body');
        // },

        format:'dd/mm/yyyy',
        // parse:null,
        // container:'body',
        firstDay:0
        // minDate:Date.now(),
        // minDate:today.getDate(),
        // minDate:new Date(),
        // maxDate:null
    });

    check_flag_notify();
    // updateTabContent(-1);
    // showTodoList();
});

function check_flag_notify() {
    // alert("Insideeee check flag method");
    // var flag_home_notification = document.getElementById('flag').value;
    // alert(flag_home_notification);
    alert('qqq'+count_dues);
    var a = count_dues;
    if (flag_home_notification===true)
    {
        alert('111'+flag_home_notification)
        // alert("Inside if check flag notify method=");
        // var session =sessionStorage.setItem("flag_home_notification",true);
        // alert("Session=",session);
        //  alert("Count Overdues=",count_overdues);
         alert("Count dues="+a);
          $('#total_overdues').html(a);
    }
    else{
        alert("Inside else ")


    }

}
function filterByDate() {
    var getdate = document.getElementById('filter_date').value;
    var tabid=$("#tabs_todo").find('li a.active').attr('id');
    var tab = tabid.replace('tab_','');
    var newtabid=parseInt(tab);
    updateTabContent(newtabid,getdate);

}

function click5(type,id)
{
    // alert("Ins
    document.getElementById('modelid').value=id;
    document.getElementById('modeltype').value=type;
    // alert(id);
    // alert(type);
    $('#modal3').modal('open');
}
function click6()
{
    var getid = document.getElementById('modelid').value;
    var gettype = document.getElementById('modeltype').value;
    var gettoken = document.getElementById('token').value;

    // alert(getid);
    // alert(gettype);
    alert(gettoken);
    $.ajax({

        url: '/todo/updatetodostatus/',
        method: "POST",
        data: {"Id":getid,"Type":gettype,"Tokenn":gettoken},
        // dataType: 'application/json; charset=utf-8',
        success:function (yes)
        {
            console.log(yes);
            alert(yes);
            alert(yes.Success);
            // token=check.Encoded;
            if(yes.Success==true)
            {

                console.log("Insideeeee succcessss offf Todo Status");
                // myemail=check.Email
                message=yes.Message;
                // alert(message);
                decoded=yes.Encodedd;
                // alert(decoded);
                window.location.href="/todo/home?Token=" + decoded;
            }
            else
            {
                console.log("Innnnsiiiideee Faaalllseee of login  jssss");

                // alert(base.Message);


                window.location.href="/todo/home";



            }
        }
    });

}
function updateTabContent(type,date)
{
    // alert(type);
    // alert(date);
    if(type===-1)
    {

        // alert("Insideee -1 1st Methoddddd");
        var gettoken = document.getElementById('token').value;
        // json={"Type":-1,"Encoded":token};
        c=getJson(type,gettoken,date);
        callAPI(c);

    }

    else if(type===0)
    {

        // alert("Insideee 0 2nd Methoddddd");
        var gettoken = document.getElementById('token').value;
        // json={"Type":-1,"Encoded":token};
        c=getJson(type,gettoken,date);
        callAPI(c);

    }

    else
    {



        var gettoken = document.getElementById('token').value;

        console.log("Date in 3 Method==",date);
        c=getJson(type,gettoken,date);
        console.log(c);
        callAPI(c);

    }

}
function getJson(value,token,date) {

    return {"Type":value,"Encoded":token,"Date":date};

}
function callAPI(JSON) {
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

function creatingATodo() {
    // alert("Inside Creating a Todo===");
    var gettitle = document.getElementById('title').value;
    var gettoken = document.getElementById('token').value;
    var getdesc = document.getElementById('desc').value;
    var getdate = document.getElementById('date').value;
    // var getselect = document.getElementById('select').value;
    // alert("Desc===",getdesc);

    // if (gettitle == null || gettitle == "") {
    //     // alert("Username must be filled out");
    //     M.toast({html: ' Title field is empty!', classes: 'rounded'});
    //     return false;
    // }
    // if (getdesc == null || getdesc == "") {
    //     // alert("Username must be filled out");
    //     M.toast({html: ' Description field is empty!', classes: 'rounded'});
    //     return false;
    // }
    // if (getdate == null || getdate == "") {
    //     // alert("Username must be filled out");
    //     M.toast({html: ' Date field is Empty!', classes: 'rounded'});
    //     return false;
    // }
    //    alert(gettitle);
    //
    //    alert(getdesc);
    //    alert(getdate);

    // else {
    $.ajax({

        url: '/todo/home/',
        method: "POST",
        data: {
            "Title": gettitle, "Desc": getdesc,
            "Datee": getdate, "Token": gettoken
        },
        dataType: 'application/json; charset=utf-8',
        success: function (base) {
            console.log(base);
            // alert(base);
            // alert(base.Success);
            // token=check.Encoded;
            if (base.Success == true) {

                console.log("Insideeeee succcessss offf LLLooogginnn");
                // myemail=check.Email
                // token = base.Token
                window.location.href = "/todo/home"
            }
            else {
                console.log("Innnnsiiiideee Faaalllseee of login  jssss");

                // alert(base.Message);
                M.toast({html: ' Todo not saved!', classes: 'rounded'});

                window.location.href = "/todo/home";


            }
        }
    });
}

