function click1() {
    var name = document.getElementById('uname').value;
    if (name==null || name=="") {
        // alert("Username must be filled out");
         M.toast({html: 'Username must be filled out!', classes: 'rounded'});
        return false;
    }
    var pswd = document.getElementById('pwd').value;
     if (pswd==null || pswd=="") {
        // alert("Password should be filled out");
         M.toast({html: 'Password must be filled out!', classes: 'rounded'});
        return false;
    }
    var email = document.getElementById('email').value;
     if (email==null || email=="") {
        // alert("Email should be filled out");
         M.toast({html: 'Email must be filled out!', classes: 'rounded'});
        return false;
    }
    var number = document.getElementById('number').value;
     if (number==null || number=="") {
        // alert("Number should be filled out");
         M.toast({html: 'Number must be filled out!', classes: 'rounded'});
        return false;
        // alert(name);
        // alert(pswd);
        // alert(email);
        // alert(number);
    }



    else {

        $.ajax({
            url: '/todo/signup/',
            method: 'POST',
            data: {"name": name, "password": pswd, "Email": email, "no": number},
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