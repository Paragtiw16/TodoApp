from __future__ import unicode_literals

from datetime import date

from django.db import models

# Create your models here.
class Userdata(models.Model):
    username = models.CharField(max_length=550, null=True, blank=True)
    password = models.CharField(max_length=550, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    contactno = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return str(self.username)

class Otpdata(models.Model):
    new = models.ForeignKey(Userdata, on_delete=models.CASCADE)
    otp = models.IntegerField(default=0)

    def __unicode__(self):
        return str(self.new.username)




class Tododata(models.Model):
    first = models.ForeignKey(Userdata, on_delete=models.CASCADE)
    title=models.CharField(max_length=550, null=True, blank=True)
    description=models.CharField(max_length=550, null=True, blank=True)
    duedate=models.DateField(default=date.today, null=True, blank=True)
    status = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.first.username)

