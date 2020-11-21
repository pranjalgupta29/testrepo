from django.db import models


# Create your models here.
class Join(models.Model):
    msg_id = models.AutoField(primary_key=True)
    oname = models.CharField(max_length=50)
    cname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    address = models.CharField(max_length=70)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    gstin = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
