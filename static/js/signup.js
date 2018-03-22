function click1() {
    var name = document.getElementById('uname').value;
    var pswd = document.getElementById('pwd').value;
    var email = document.getElementById('email').value;
    var number = document.getElementById('number').value;
    alert(name);
    alert(pswd);
    alert(email);
    alert(number);
    $.ajax({
        url: '/todo/signup/',
        method: 'POST',
        data: {"name": name, "password": pswd, "Email": email, "no": number},
        // dataType: 'application/json; charset=utf-8',
         success:function (text) {
                   alert("Mmmmmmmeeeeessssaaagggeeee");
                   console.log(text);
                    alert(text);
                   if(text.Success==true)
                   {
                       console.log(text.Email);
                       get_email=text.Email;
                       window.location.href="/todo/otppage?Email="+get_email
                       // "Email":get_email

                   }


         }
    });
}