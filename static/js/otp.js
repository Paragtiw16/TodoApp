
$(document).ready(function () {


    $('#frmm input').keydown(function (e) {
        if (e.keyCode == 13) {
            $('#frmm').trigger(click2())
        }
    });

});









function click2() {
    var get_otp = document.getElementById('otp').value;
    if (get_otp==null || get_otp=="") {
        // alert("Username must be filled out");
         M.toast({html: 'Please enter OTP!', classes: 'rounded'});
        return false;
    }
    var myemail = document.getElementById('emmail').value;

    // alert(get_otp);

    // alert(myemail);

    $.ajax({

        url: '/todo/otppage/',
        method: "POST",
        // data: {"Otp": otp, "Email": get_email},
        data: {"Otp": get_otp, "Email": myemail},

        // dataType: 'application/json; charset=utf-8',
        success: function (script) {
            // alert("HHHHHHHHEEEEEEEELLLLLLLLOOOOOOOOO");
            // console.log(script);
            // alert(script);
            // alert(script.Success);
            if (script.Success == true) {
                console.log("Insideee successsss off successs of otp");
                window.location.href = "/todo/login_login";
            }
            else {
                // console.log("Innnnsiiiideee Faaalllseee");
                // console.log(script.Message);
                // get_msg = script.Message;
                 M.toast({html: 'Please enter Correct OTP!', classes: 'rounded'});
                // console.log(script.Email);
                myemaill = script.Email;
                console.log(myemaill);
                // window.location.href = "/todo/otppage?&MyEmail=" + myemaill


            }

        }
    });
}
