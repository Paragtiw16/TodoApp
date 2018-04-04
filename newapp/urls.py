
from django.conf.urls import url

from newapp.views import signup, login_login, otppage, home, profile, display, updatetodostatus, side, user_logout

urlpatterns = [


    url(r'^signup/$',signup ),
    url(r'^$',login_login),
    url(r'^login_login/$',login_login),
    url(r'^otppage/$',otppage),
    url(r'^home/$',home),
    url(r'^display/$', display),
    url(r'^profile/$',profile),
    url(r'^updatetodostatus/$',updatetodostatus),
    url(r'^side/$',side),
    url(r'^user_logout/$',user_logout)




    # url(r'^edit/$',edit)

    ]