from django.contrib import admin

# Register your models here.
from newapp.models import Userdata, Otpdata, Tododata

admin.site.register(Userdata)
admin.site.register(Otpdata)
admin.site.register(Tododata)
