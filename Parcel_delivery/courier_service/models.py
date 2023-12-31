from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user_details(models.Model):
    UserId=models.IntegerField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Contact_Number=models.BigIntegerField(default=0)
    Email=models.EmailField(default='null')
    House_No=models.CharField(max_length=50,default='null')
    Street=models.CharField(max_length=50,default='null')
    City=models.CharField(max_length=50,default='null')
    State=models.CharField(max_length=50,default='null')
    Pin_Code=models.IntegerField(default=0)
    
class Branches(models.Model):
    Branch_Id=models.IntegerField(primary_key=True)
    Branch_Name=models.CharField(max_length=50)
    Contact_Number=models.BigIntegerField()
    Email=models.EmailField()
    House_No=models.CharField(max_length=50)
    Street=models.CharField(max_length=50)
    City=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    Pin_Code=models.IntegerField()

class Department(models.Model):
    Department_Id=models.IntegerField(primary_key=True)
    Department_Name=models.CharField(max_length=50)

class Employees(models.Model):
    Employee_Id=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    Contact_Number=models.BigIntegerField()
    Email=models.EmailField()
    House_No=models.CharField(max_length=50)
    Street=models.CharField(max_length=50)
    City=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    Pin_Code=models.IntegerField()
    Salary=models.IntegerField()
    Branch_Id=models.ForeignKey(Branches,null=True,on_delete=models.CASCADE)
    Department_Id=models.ForeignKey(Department,null=True,on_delete=models.CASCADE)
    Manager_Id= models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE)
class cities(models.Model):
    name=models.CharField(max_length=50)
    latitude=models.FloatField()
    longitude=models.FloatField()

class Orders(models.Model):
    Order_Id=models.IntegerField(primary_key=True)
    Order_Name=models.CharField(max_length=50)
    Parcel_Weight=models.IntegerField()
    Parcel_length=models.IntegerField(null=True,blank=True)
    Parcel_Width=models.IntegerField(null=True,blank=True)
    Parcel_height=models.IntegerField(null=True,blank=True)
    booked_date=models.DateTimeField()
    shipped_date=models.DateTimeField(null=True,blank=True)
    delivered_date=models.DateTimeField(null=True,blank=True)
    From_House_No=models.CharField(max_length=50)
    From_Street=models.CharField(max_length=50)
    From_City=models.CharField(max_length=50)
    From_State=models.CharField(max_length=50)
    From_Pin_Code=models.IntegerField()
    Receiver_Name=models.CharField(max_length=50)
    Receiver_Contact_Number=models.BigIntegerField()
    To_House_No=models.CharField(max_length=50)
    To_Street=models.CharField(max_length=50)
    To_City=models.CharField(max_length=50)
    To_State=models.CharField(max_length=50,null=True)
    To_Pin_Code=models.IntegerField()
    Order_Status=models.CharField(max_length=50,default="Not yet delivered.")
    Order_location=models.ForeignKey(cities,on_delete=models.CASCADE,null=True,blank=True)
    Order_Type=models.CharField(max_length=50)
    delivery_charge=models.IntegerField(null=True,blank=True)
    User_Id=models.ForeignKey(user_details,on_delete=models.CASCADE,null=True,blank=True)
    Sender_Employee_Id=models.ForeignKey(Employees,related_name='employee1',on_delete=models.CASCADE,null=True,blank=True)
    Receiver_Name_Employee_Id=models.ForeignKey(Employees,related_name='employee2',on_delete=models.CASCADE,null=True,blank=True)

class Contacts(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.TextField()
