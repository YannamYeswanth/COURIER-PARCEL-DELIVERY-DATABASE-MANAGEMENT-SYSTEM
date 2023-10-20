from django.db import models

# Create your models here.
class User(models.Model):
    UserId=models.IntegerField()
    name=models.CharField(max_length=50)
    Contact_Number=models.BigIntegerField()
    Email=models.EmailField()
    House_No=models.CharField(max_length=50)
    Street=models.CharField(max_length=50)
    City=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    Pin_Code=models.IntegerField()
    