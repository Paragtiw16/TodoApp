function click3() {


    var get_email = document.getElementById('email').value;
    var get_pwd = document.getElementById('pwd').value;

    alert(get_email);
    alert(get_pwd);

    $.ajax({

        url: '/todo/login_login/',
        method: "POST",
        data: {"Password": get_pwd, "Email": get_email},
        // dataType: 'application/json; charset=utf-8',
        success:function (check) {
                    console.log(check);
                    alert(check);
                    alert(check.Success);
                    token=check.Encoded;
             if(check.Success==true)
                   {

                       console.log("Insideeeee succcessss offf LLLooogginnn");
                       // myemail=check.Email
                       window.location.href="/todo/home?Token="+token;
                   }
             else
                    {
                        console.log("Innnnsiiiideee Faaalllseee of login  jssss");
                        console.log(check.Message);
                        alert(check.Message);

                        window.location.href="/todo/login_login";



                      }
        }
    });
}