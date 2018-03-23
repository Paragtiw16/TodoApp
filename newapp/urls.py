
from django.conf.urls import url

from newapp.views import signup, login_login, otppage, home, profile, display

urlpatterns = [


    url(r'^signup/$',signup ),
    url(r'^login_login/$',login_login),
     url(r'^otppage/$',otppage),
     url(r'^home/$',home),
    url(r'^display/$', display),
    url(r'^profile/$',profile)


    # url(r'^edit/$',edit)

    ]