
$(document).ready(function () {


    $('#fr input').keydown(function (e) {
        if (e.keyCode == 13) {
            $('#fr').trigger(click3())
        }
    });

});







function click3() {


    var get_email = document.getElementById('email').value;
    if (get_email == null || get_email == "") {
        // alert("Username must be filled out");
        M.toast({html: 'Email should be filled out!', classes: 'rounded'});
        return false;
    }
    var get_pwd = document.getElementById('pwd').value;
    if (get_pwd == null || get_pwd == "") {
        // alert("Username must be filled out");
        M.toast({html: 'Password must be filled out!', classes: 'rounded'});
        return false;
    }

    // alert(get_email);
    // alert(get_pwd);

    else {


        $.ajax({

            url: '/todo/login_login/',
            method: "POST",
            data: {"Password": get_pwd, "Email": get_email},
            // dataType: 'application/json; charset=utf-8',
            success: function (check) {
                // console.log(check);
                // alert(check);
                // alert(check.Success);
                token = check.Encoded;
                if (check.Success == true) {

                    console.log("Insideeeee succcessss offf LLLooogginnn");
                    // myemail=check.Email
                    window.location.href = "/todo/home?Token=" + token;
                }
                else {
                    // console.log("Innnnsiiiideee Faaalllseee of login  jssss");
                    // console.log(check.Message);
                    msg=(check.Message);
                    M.toast({html: 'Please enter Correct Username and Password!', classes: 'rounded'});
                    // window.location.href = "/todo/login_login";


                }
            }
        });
    }
}