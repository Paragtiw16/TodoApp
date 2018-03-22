import datetime
import jwt
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.crypto import random
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from newapp.models import Userdata,Otpdata,Tododata


@csrf_exempt
def signup(request):
    if request.method == "GET":
        return render(request, "signup.html")
    elif request.method == "POST":
        print("inside signup POST Method")
        get_uname = request.POST.get('name')
        get_pwd = request.POST.get('password')
        get_email = request.POST.get('Email')
        get_number = request.POST.get('no')
        print("get_uname ", get_uname)
        print("get_email ", get_email)
        for x in range(1000, 9999):

            Otp = random.randint(1000, 9999)
            print("Myyyyy Ottttppppppp=====", Otp)
            break


        try:

            login_details = Userdata.objects.create(username=get_uname, password=get_pwd,
                                                  email=get_email, contactno=get_number)
            match_details =Otpdata.objects.create(otp=Otp, new=login_details)
            todo_details=Tododata.objects.create(first=login_details)

        except Exception, e:
            print("Our Error=", str(e))

        print("Number=", get_number)

        request.session['Email'] = get_email
    return JsonResponse({"Email": get_email, "Success": True})

@csrf_exempt
def otppage(request):
    if request.method == "GET":
        print('OOOOOOOOOOTTTTTTTTTTPPPPPPPP')
        myemail = request.GET.get('Email')
        mymsg =request.GET.get('Message')

        if myemail is None:
            print("Inssssiiiiideeeee Faaalllseee case IIIFFFFF")
            femail=request.GET.get('MyEmail')
            print("False caseeeeeee Emmmaaaailllll=====",femail)
            myemail=femail
            print("Assssssssssiiiignnnnnmmmeeennntttttt===",myemail)
        return render(request, "otp.html",{"Email": myemail,"Message": mymsg})
    elif request.method == "POST":
        myotp = request.POST.get('Otp')
        myemaill =request.POST.get('Email')
        print("My Otp========",myotp)
        if Userdata.objects.filter(email=myemaill).exists():

            print("Inside ifffffffffff")
            data1 = Userdata.objects.get(email=myemaill)
            print("DDDDDDDDDDDDDDDDDDDAAAAATTTTAAAAAA111111",data1)
            data2 =Otpdata.objects.get(new=data1)
            dbotp =data2.otp
            print("MMMMMMMMMYYYYYYYYYYYOOOOTTTTTTPPPPPP",dbotp)
            print("MMMMMMMMMYYYYYYYYYYYOOOOTTTTTTPPPPPP",int(myotp))
            if int(myotp)==dbotp:
                print("Inside Trrrrrrrrrrrruuuuuuuueeeeeeeeeeee")
                del request.session['Email']
                # print("Sesssionn Emmmaaillll=",get_email)
                # request.session['Email'] = get_email
                return JsonResponse({"Message": "success", "Success": True})
            else:
                print("Inside Fallllllssssssseeeeeee")
                msg = "Please enter correct otp"
                print("Fallllseeee Emmmaailllll=====", myemaill)
                return JsonResponse({"Message": msg, "Success": False,"Email":myemaill})


@csrf_exempt
def login_login(request):
    print("Checking loginnnn Conditionnnnnn")
    if request.method == "GET":
        print("Innnnnsssiiiiiidddeee Lllllooogggiiinnnn   GGGETTT")
        # mymsg = request.GET.get('Message')
        # print("Alerrrrtttt messageeeee",mymsg)
        return render(request, "Login.html")
    elif request.method == "POST":
        print("Insiddeeeeee llooooogggiiinnn POOOOSSTTT")
        myemail=request.POST.get('Email')
        mypassword=request.POST.get('Password')
        print("User entered Email=", myemail)
        print("User entered Password=", mypassword)
        flag=Userdata.objects.filter(email=(myemail)).exists()
        if flag==True:
                print("Insideee Flaggggggggggggg")

                data1=Userdata.objects.get(email=myemail)

                email=data1.email
                print("Database email=", email)
                pssword=data1.password
                print("Database password=", pssword)
                id=data1.id


                if   pssword==mypassword:

                    print("MyEmail==",myemail)
                    key = 'secret'
                    encoded=jwt.encode({'email':myemail,'Id':id},key,algorithm='HS256')
                    # request.session['Encoded'] =encoded
                    print("afterrr ennncoooddingggg")
                    return JsonResponse({"Message": "success", "Success": True,
                                         "Encoded":encoded})
                else:
                    print("Inside else incorrect detailssss")
                    msg="Please enter correct Details"
                    print("Messaaggeeeeee=",msg)
                    return JsonResponse({"Message": msg, "Success": False})

        else:
            print("Inside else incorrect detailssss")
            msg = "Please enter correct Details"
            print("Messaaggeeeeee=", msg)
            return JsonResponse({"Message": msg, "Success": False})


@csrf_exempt
def home(request):
    if request.method == "GET":
        # print('OOOOOOOOOOTTTTTTTTTTPPPPPPPP')
         print("Insideeeeeeeeeee HOOOOOOOOMEEEEEE")
         key = 'secret'
         encoded=request.GET.get('Token')
         print("getting encoding value=",encoded)
         decoded = jwt.decode(encoded, key, algorithms='HS256')
         encoded = jwt.encode(decoded, key, algorithm='HS256')

         print("Decodedddddddd Jsssooonnnn=",decoded)
         ID=decoded['Id']
         print("Idddddd=====",ID)
         try:

             data1 = Userdata.objects.get(id=ID)
         except Exception, e:
               print("Apna  Error=", str(e))
         print(data1)
         username=data1.username
         email =data1.email
         contactno=data1.contactno
         encoded = jwt.encode(decoded, key, algorithm='HS256')
         return render(request, "home.html",{"Email":email,"Username":username,
                                              "Contact_no":contactno,"Encoded":encoded})
    elif request.method == "POST":
        print("Insiddeeeeee llooooogggiiinnn POOOOSSTTT")
        mytitle = request.POST.get('Title')
        print("Title=",mytitle)
        # myselect = request.POST.get('Select')
        # print("Select Field=",myselect)
        mydesc = request.POST.get('Desc')
        print("Description=",mydesc)
        mydate = request.POST.get('Date')
        print("Dateeeeee=",mydate)
        # gettoken = request.POST.get('Token')
        # defaultdate=datetime.date.today
        # print("Deeeefaaullltttt Dayyyyyy=",defaultdate)
        datee=datetime.datetime.strptime(mydate, '%d/%m/%Y').strftime('%Y-%m-%d')
        print("Date Object=====",datee)
        # print("Tokennnnnn======",gettoken)
        # if mydate< datetime.date.today():
        #     msg = "Please enter correct Date Format"
        #     print("Messaaggeeeeee=", msg)
        #     return JsonResponse({"Message": msg, "Success": False})
        # else:
        key = 'secret'
        encoded = request.POST.get('Token')
        print("getting encoding value=", encoded)
        decoded = jwt.decode(encoded, key, algorithms='HS256')
        encoded = jwt.encode(decoded, key, algorithm='HS256')

        print("Decodedddddddd Jsssooonnnn=", decoded)
        ID = decoded['Id']
        print("Idddddd=====", ID)
        try:

            data1 = Userdata.objects.get(id=ID)
        except Exception, e:
            print("Apna  Error=", str(e))
        print(data1)
        # username = data1.username
        # email = data1.email
        tododetails=Tododata.objects.create(first=data1,title=mytitle, description=mydesc ,
                                    duedate =datee)
        print("Returningggg successssssssssssss")
        return JsonResponse({"Token": encoded, "Success": True})



def profile(request):
    if request.method == "GET":
        # print('OOOOOOOOOOTTTTTTTTTTPPPPPPPP')
         print("Insideeeeeeeeeee Profileeeee")
         key = 'secret'
         encoded=request.GET.get('Token')
         print("getting encoding value=",encoded)
         decoded = jwt.decode(encoded, key, algorithms='HS256')
         encoded = jwt.encode(decoded, key, algorithm='HS256')

         print("Decodedddddddd Jsssooonnnn=",decoded)
         ID=decoded['Id']
         print("Idddddd=====",ID)
         try:

             data1 = Userdata.objects.get(id=ID)
         except Exception, e:
               print("Apna  Error=", str(e))
         print(data1)
         username=data1.username
         email =data1.email
         contactno=data1.contactno
         encoded = jwt.encode(decoded, key, algorithm='HS256')
         return render(request, "profile.html",{"Email":email,"Username":username,
                                              "Contact_no":contactno,"Encoded":encoded})




