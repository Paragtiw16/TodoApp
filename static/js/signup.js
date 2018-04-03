function click1() {
    var name = document.getElementById('uname').value;
    if (name===null || name==="") {
        // alert("Username must be filled out");
        M.toast({html: 'Username must be filled out!', classes: 'rounded'});
        return false;
    }

    var pswd1 = document.getElementById('pwd1').value;
    var pswd2 = document.getElementById('pwd2').value;
    if (pswd1!==pswd2){
        M.toast({html: 'Password did not match', classes: 'rounded'});
        return false;
    }
    if (pswd1===null || pswd1==="") {
        // alert("Password should be filled out");
        M.toast({html: 'Password must be filled out!', classes: 'rounded'});
        return false;
    }
    re = /[0-9]/;
    if(!re.test(pswd1))
    {
        M.toast({html: 'Password must contain atleast one number!', classes: 'rounded'});
        return false;
    }

    re =  /[a-z]/;
    if(!re.test(pswd1))
    {
        M.toast({html: 'Password must contain atleast lower case letter!', classes: 'rounded'});
        return false;
    }
    re = /[A-Z]/;
    if(!re.test(pswd1))
    {
        M.toast({html: 'Password must contain atleast Upper case letter', classes: 'rounded'});
        return false;
    }

    var email = document.getElementById('email').value;
    if (email==null || email=="") {
        // alert("Email should be filled out");
        M.toast({html: 'Email must be filled out!', classes: 'rounded'});
        return false;
    }


    var number = document.getElementById('mobile_number').value;
    if (number===null || number==="" ) {
        alert(number);
        // alert("Number should be filled out");
        M.toast({html: 'Number must be filled out!', classes: 'rounded'});
        return false;
    }
    if (number.length!==10){
        // alert(number.length);
        M.toast({html: 'Number must be of 10 Digits', classes: 'rounded'});
        return false;
    }




    else {

        $.ajax({
            url: '/todo/signup/',
            method: 'POST',
            data: {"name": name, "password": pswd1, "Email": email, "no": number},
            // dataType: 'application/json; charset=utf-8',
            success: function (text) {
                // alert("Mmmmmmmeeeeessssaaagggeeee");
                // console.log(text);
                // alert(text);
                if (text.Success == true) {
                    console.log(text.Email);
                    get_email = text.Email;
                    window.location.href = "/todo/otppage?Email=" + get_email
                    // "Email":get_email

                }


            }
        });
    }
}





$(document).ready(function () {


    $('#frm input').keydown(function (e) {
        if (e.keyCode == 13) {
            $('#frm').trigger(click1())
        }
    });

});
