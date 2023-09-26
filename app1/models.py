from django.db import models

# Create your models here.
class user(models.Model):
    unmane=models.CharField(max_length=50)
    upassword=models.CharField(max_length=50)
    uemail=models.CharField(max_length=50)

class Meta:
    db_table='users'
