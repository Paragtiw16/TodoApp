import datetime
import jwt
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import Context
from django.template.loader import get_template
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
            # todo_details=Tododata.objects.create(first=login_details)

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
                    request.session['Encoded'] =encoded
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
         # encoded = jwt.encode(decoded, key, algorithm='HS256')

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
        mydesc = request.POST.get('Desparagtiwari314@gmail.comc')
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
@csrf_exempt
def display(request):
    if request.method == "GET":
        print("Insideeeee displayyy GETTTTTTTTTT")
        mytype = request.GET.get('Type')
        Mytype=int(mytype)
        print("TYYYPEEEEE=",Mytype)
        token = request.GET.get('Encoded')
        print("My tokennnnnn==",token)
        mydate = request.GET.get('Date')
        print("Dateeeee===",mydate)
        key = 'secret'
        decoded = jwt.decode(token, key, algorithms='HS256')
        encoded = jwt.encode(decoded, key, algorithm='HS256')
        if mydate=='' or mydate==None:
            print("Inside blank mydateeeeeeeee")
            # datee = datetime.datetime.strptime(mydate, '%d/%m/%Y').strftime('%Y-%m-%d')
            ID = decoded['Id']
            data1 = Userdata.objects.get(id=ID)
            print("Data1", data1)
            # data2 =Tododata.objects.get(first=data1)
            # myduedate=data2.duedate
            # print("All duedates===",myduedate)
            # mystatus=data2.status
            # print("All Status===",mystatus)
            nowdate = datetime.datetime.today().date()
            print("Nowwww dateeeee===", nowdate)
            datee = datetime.datetime.strptime(str(nowdate), ('%Y-%m-%d')).strftime('%Y-%m-%d')
            print("Comaparedd Date===", datee)
            print("Outsideeeee ifffff")
            if Mytype == -1:
                print("Insideeeee Ifffffffffffff")
                # nowdate=datetime.datetime.today().date()
                # print("Nowwww dateeeee===",nowdate)
                # datee = datetime.datetime.strptime(str(nowdate), ('%Y-%m-%d')).strftime('%Y-%m-%d')
                # print("Comaparedd Date===",datee)
                qdata1 = Tododata.objects.filter(first=data1, status=False,
                                                 duedate__lt=nowdate)
                print("Query Set for -11111=", qdata1)
                bjson = []
                try:

                    for i in qdata1:
                        ostatus = i.status
                        oduedate = i.duedate
                        odesc = i.description
                        otitle = i.title
                        Id = i.id
                        createddate=i.created_date
                        print("After loop status==", ostatus)
                        print("After loop duedate==", oduedate)
                        print("After loop desc==", odesc)
                        print("After loop title==", otitle)
                        print("Id====", Id)
                        tempjson = {"Status": ostatus, "Duedate": oduedate, "Desc": odesc,
                                    "Title": otitle, "ID": Id,"Cdate":createddate}

                        bjson.append(tempjson)
                    print("Bjsoonnn=", bjson)
                except Exception, e:
                    print("Our Error=", str(e))
                template = get_template('show.html')
                print("TYYYPEEEEE=", Mytype)
                context = Context({"Bjson": bjson, "Success": True, "Encoded": encoded,
                                   "Type": Mytype})
                html = template.render(context)
                return HttpResponse(html)
            elif Mytype==0:
                print("Insideee O functionality")
                qdata2 = Tododata.objects.filter(first=data1,status=False,
                                                         duedate__gte=nowdate,complete_date=datee)
                print("Query set for 00000==",qdata2)
                bjson = []
                for i in qdata2:
                    ostatus = i.status
                    oduedate = i.duedate
                    odesc = i.description
                    otitle = i.title
                    createddate = i.created_date
                    print("After loop status==", ostatus)
                    print("After loop duedate==", oduedate)
                    print("After loop desc==", odesc)
                    print("After loop title==", otitle)
                    tempjson = {"Status": ostatus, "Duedate": oduedate, "Desc": odesc,
                                "Title": otitle,"Cdate":createddate}

                    bjson.append(tempjson)
                print("Bjsoonnn=", bjson)
                template = get_template('show.html')
                print("TYYYPEEEEE=", Mytype)
                context = Context({"Bjson": bjson, "Success": True, "Encoded": encoded,
                                   "Type": Mytype})
                html = template.render(context)
                return HttpResponse(html)
            else:
                print("Insidee 111 FUNCTIONALITY")
                qdata3=Tododata.objects.filter(first=data1,status=True)
                print("Query set for 11111====",qdata3)
                bjson = []
                for i in qdata3:
                    ostatus = i.status
                    oduedate = i.duedate
                    odesc = i.description
                    otitle = i.title
                    Iddd=i.id
                    createddate = i.created_date
                    print("After loop status==", ostatus)
                    print("After loop duedate==", oduedate)
                    print("After loop desc==", odesc)
                    print("After loop title==", otitle)
                    print("Idddddddddddddd=",Iddd)

                    tempjson = {"Status": ostatus, "Duedate": oduedate, "Desc": odesc,
                                "Title": otitle,"Cdate":createddate}

                    bjson.append(tempjson)
                print("Bjsoonnn=", bjson)
                template = get_template('show.html')
                print("TYYYPEEEEE=", Mytype)
                context = Context({"Bjson": bjson, "Success": True, "Encoded": encoded,
                                   "Type": Mytype})
                html = template.render(context)
                return HttpResponse(html)


        else:
            print("insideee else my dateeeeee")
            datee = datetime.datetime.strptime(mydate, '%d/%m/%Y').strftime('%Y-%m-%d')
            print("Changed Format===",datee)
            ID = decoded['Id']
            data1 = Userdata.objects.get(id=ID)
            print("Data1",data1)
            # data2 =Tododata.objects.get(first=data1)
            # myduedate=data2.duedate
            # print("All duedates===",myduedate)
            # mystatus=data2.status
            # print("All Status===",mystatus)
            nowdate = datetime.datetime.today().date()
            print("Nowwww dateeeee===", nowdate)
            # datee = datetime.datetime.strptime(str(nowdate), ('%Y/%m/%d')).strftime('%Y-%m-%d')
            # print("Comaparedd Date===", datee)
            print("Outsideeeee ifffff")
            if Mytype==-1:
                print("Insideeeee Ifffffffffffff")
                # nowdate=datetime.datetime.today().date()
                # print("Nowwww dateeeee===",nowdate)
                # datee = datetime.datetime.strptime(str(nowdate), ('%Y-%m-%d')).strftime('%Y-%m-%d')
                # print("Comaparedd Date===",datee)
                qdata1= Tododata.objects.filter(first=data1,status=False,
                                                duedate__lt=nowdate,created_date=datee)
                print("Query Set for -11111=",qdata1)
                bjson =[]
                try:

                    for i in qdata1:
                          ostatus=i.status
                          oduedate=i.duedate
                          odesc=i.description
                          otitle=i.title
                          Id=i.id

                          print("After loop status==",ostatus)
                          print("After loop duedate==",oduedate)
                          print("After loop desc==", odesc)
                          print("After loop title==", otitle)
                          print("Id====",Id)
                          tempjson={"Status":ostatus,"Duedate":oduedate,"Desc":odesc,
                                    "Title":otitle,"ID":Id}
                          print("Temp Jsonnnn=",tempjson)
                          bjson.append(tempjson)
                    print("Bjsoonnn=",bjson)
                except Exception, e:
                    print("Our Error=", str(e))
                template=get_template('show.html')
                print("Type===",Mytype)
                context=Context({"Bjson":bjson,"Success": True, "Encoded":encoded,
                                 "Type":Mytype})
                html=template.render(context)
                return HttpResponse(html)


            # encoded = jwt.encode(decoded, key, algorithm='HS256')
            # return render_to_response("show.html",{"Bjson":bjson,"Success": True,
            #                                        "Encoded":encoded})
            # return render(request,"show.html",{"Bjson":bjson})

            elif Mytype==0:
                print("Insideee O functionality")
                qdata2 = Tododata.objects.filter(first=data1,status=False,
                                                         duedate__gte=nowdate,complete_date=datee)
                print("Query set for 00000==",qdata2)
                bjson = []
                for i in qdata2:
                    ostatus = i.status
                    oduedate = i.duedate
                    odesc = i.description
                    otitle = i.title
                    print("After loop status==", ostatus)
                    print("After loop duedate==", oduedate)
                    print("After loop desc==", odesc)
                    print("After loop title==", otitle)
                    tempjson = {"Status": ostatus, "Duedate": oduedate, "Desc": odesc,
                                "Title": otitle}

                    bjson.append(tempjson)
                print("Bjsoonnn=", bjson)
                template = get_template('show.html')
                context = Context({"Bjson":bjson,"Success": True, "Encoded":encoded,
                                 "Type":Mytype})
                html = template.render(context)
                return HttpResponse(html)
            else:
                print("Insidee 111 FUNCTIONALITY")
                qdata3=Tododata.objects.filter(first=data1,status=True,created_date=datee)
                print("Query set for 11111====",qdata3)
                bjson = []
                for i in qdata3:
                    ostatus = i.status
                    oduedate = i.duedate
                    odesc = i.description
                    otitle = i.title
                    Iddd=i.id
                    print("After loop status==", ostatus)
                    print("After loop duedate==", oduedate)
                    print("After loop desc==", odesc)
                    print("After loop title==", otitle)
                    print("Idddddddddddddd=",Iddd)
                    tempjson = {"Status": ostatus, "Duedate": oduedate, "Desc": odesc,
                                "Title": otitle}

                    bjson.append(tempjson)
                print("Bjsoonnn=", bjson)
                template = get_template('show.html')
                context = Context({"Bjson":bjson,"Success": True, "Encoded":encoded,
                                 "Type":Mytype})
                html = template.render(context)
                return HttpResponse(html)

@csrf_exempt
def updatetodostatus(request):
    if request.method == "POST":
        print("Insideeeee todostatus POSTTTTTTTTT")
        myid= request.POST.get('Id')
        print("Id======",myid)
        mytype = request.POST.get('Type')
        print("Typeee====",mytype)
        data1 = Tododata.objects.get(id=myid)
        print("Instance of Todo TABLE=====",data1)
        nowdate = datetime.datetime.today().date()
        # qdata1 = Tododata.objects.get(first=data1, status=True,
        #                                  complete_date=nowdate)
        data1.status=True
        data1.complete_date=nowdate
        data1.save()
        msg="This Todo has been completed"
        return JsonResponse({"Message":msg, "Success": True})





