



$(document).ready(function () {
    $('.tabs').tabs();
    $('.modal').modal();
     $('#modal3').modal();
    //  $('#modal').modal('type','id');
    $('select').formSelect();

    $('.datepicker').datepicker({
        format:'dd/mm/yyyy',
        parse:null,
        container:'body',
        firstDay:0,
        // minDate:Date.now(),
        // minDate:today.getDate(),
        // minDate:new Date(),
        maxDate:null});
        updateTabContent(-1);


});
function filterByDate() {
    console.log("Inside filter by date");
    var getdate = document.getElementById('filter_date').value;
    var tabid=$("#tabs_todo").find('li a.active').attr('id');
    // var getting = browser.tabs.get(integer. (-1));
//     $('.tabs').click(function(){
// var a=$(this).attr('id');
// $('#sample').html('Active Tab is'+a);
// });
//     var tabid=$('.tabs. active').id;
//     alert(tabid);
    console.log("Tab Id=",tabid);
   var tab = tabid.replace('tab_','');
    console.log("Tab Id=",tab);
    var newtabid=parseInt(tab);
    console.log("new Tab Id=",newtabid);
//     alert(getting);
    alert(getdate);
    updateTabContent(newtabid,getdate);

}
 function click5(type,id)
 {
     // alert("Inside Status function");
     // alert(type);
     // alert(id);
     document.getElementById('modelid').value=id;
     document.getElementById('modeltype').value=type
     $('#modal3').modal('open');
     // var getid = document.getElementById('id').value;
     // alert(getid)
     // var gettype = document.getElementById('type').value;
     // alert(gettype)
     // $('.modal2').modal('open');



 }
 function click6()
 {
      var getid = document.getElementById('modelid').value;
    var gettype = document.getElementById('modeltype').value;
     // alert(getid);
     // alert(gettype);
     $.ajax({

        url: '/todo/updatetodostatus/',
        method: "POST",
        data: {"Id":getid,"Type":gettype},
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
                alert(message);

                // window.location.href="/todo/profile?Token="+token;
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

        // alert("Insideee 1 3rd Methoddddd");

         var gettoken = document.getElementById('token').value;
        // json={"Type":-1,"Encoded":token};
        // alert(type);
        // alert(date);
        console.log("Date in 3 Method==",date);
        c=getJson(type,gettoken,date);
        console.log(c);
         callAPI(c);

    }

}
function getJson(value,token,date) {
    // alert("Inside Secondd Methoddd");
    return {"Type":value,"Encoded":token,"Date":date};

}
function callAPI(JSON) {
    // alert("Callinggg APPIIIIIII");
    // alert("JSONNNNNNN=",JSON);
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


    if (gettitle == null || gettitle == "") {
        // alert("Username must be filled out");
        M.toast({html: ' Title field is empty!', classes: 'rounded'});
        return false;
    }
    if (getdesc == null || getdesc == "") {
        // alert("Username must be filled out");
        M.toast({html: ' Description field is empty!', classes: 'rounded'});
        return false;
    }
    if (getdate == null || getdate == "") {
        // alert("Username must be filled out");
        M.toast({html: ' Date field is Empty!', classes: 'rounded'});
        return false;
    }


    else {
        $.ajax({

            url: '/todo/home/',
            method: "POST",
            data: {
                "Title": gettitle, "Desc": getdesc,
                "Date": getdate, "Token": gettoken
            },
            // dataType: 'application/json; charset=utf-8',
            success: function (base) {
                console.log(base);
                // alert(base);
                // alert(base.Success);
                // token=check.Encoded;
                if (base.Success == true) {

                    console.log("Insideeeee succcessss offf LLLooogginnn");
                    // myemail=check.Email
                    token = base.Token
                    window.location.href = "/todo/home?Token=" + token;
                }
                else {
                    console.log("Innnnsiiiideee Faaalllseee of login  jssss");

                    // alert(base.Message);


                    window.location.href = "/todo/home";


                }
            }
        });
    }
}

// function validateForm() {
//     var x = document.forms["myForm"]["fname"].value;
//     if (x == "") {
//         alert("Name must be filled out");
//         return false;
//     }
// }
