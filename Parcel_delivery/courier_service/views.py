from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.shortcuts import redirect
from datetime import datetime
from .models import User,Orders


# Create your views here.

def home(request):
    return render(request, 'Home.html')
# def login(request):
    # return render(request, 'Login.html')
def ContactUs(request):
    return render(request, 'ContactUs.html')
def About(request):
    return render(request, 'About.html')
def Help(request):
    return render(request, 'Help.html')
def place_parcel(request):
    if request.method=='POST':
        ordername=request.POST.get('ordername')
        weight=request.POST.get('weight') 
        deliverymode=request.POST.get('deliverymode')
        receivername=request.POST.get('receivername')
        houseno=request.POST.get('houseno')
        street=request.POST.get('street')
        city=request.POST.get('city')
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')
        houseno2=request.POST.get('houseno2')
        street2=request.POST.get('street2')
        city2=request.POST.get('city2')
        state2=request.POST.get('state2')
        pincode2=request.POST.get('pincode2')
        orders=Orders.objects.all()
        n=len(orders)+1
        Curr_datetime=datetime.now()
        User_Id =User.objects.get(id=request.user.id)
        neworder=Orders.objects.create(Order_Id=n,Order_Name=ordername,Parcel_Weight=weight,booked_date=Curr_datetime,From_House_No=houseno,From_Street=street,From_City=city, From_State=state,From_Pin_Code=pincode,Receiver_Name=receivername,To_House_No=houseno2,To_Street=street2,To_City=city2,To_State=state2,To_Pin_Code=pincode2,Order_Type=deliverymode,User_Id=User_Id)        
        neworder.save()
        
    return render(request, 'place_parcel.html')
def track_parcel(request):
    return render(request, 'parcel.html')
def estimate(request):
    return render(request, 'estimate.html')
