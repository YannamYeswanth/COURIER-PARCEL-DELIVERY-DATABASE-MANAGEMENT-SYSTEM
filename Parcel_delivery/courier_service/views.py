<<<<<<< Updated upstream
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.shortcuts import redirect
from datetime import datetime
from .models import User,Orders


=======
from django.shortcuts import render,redirect
from courier_service.models import user_details
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
>>>>>>> Stashed changes
# Create your views here.

def home(request):
    return render(request, 'Home.html')
def Login(request):
    if request.method=='POST':
        name=request.POST.get('username')
        pas=request.POST.get('password')
        user=authenticate(username=name, password=pas)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.warning(request, 'Wrong Username or password')
            return render(request, 'login.html')
    return render(request,'login.html')
def signup(request):
      if request.method=="POST":
        name=request.POST.get('username')
        pas1=request.POST.get('pas1')
        pas2=request.POST.get('pas2')
        
        if pas1!=pas2:
            messages.warning(request, 'password not same')
            return render(request, 'signup.html')
        
        user=User.objects.create(username=name,password=make_password(pas1))
        user.save()
        user_det=user_details.objects.create(user=user)
        user_det.save()
        users=authenticate(username=name, password=pas1)
        if users is not None:
            login(request,users)
            return redirect('signupxtra')
      return render(request,'signup.html')
def signupxtra(request):
    if request.method=="POST":
        h_no=request.POST.get('H_No')
        street=request.POST.get('street')
        city=request.POST.get('city')
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')
        email=request.POST.get('email')
        contact=request.POST.get('c_no')
        user=request.user
        new_user=user_details.objects.filter(user=user)[0]
        new_user.Contact_Number=contact
        new_user.City=city
        new_user.State=state
        new_user.Pin_Code=pincode
        new_user.Street=street
        new_user.House_No=h_no
        new_user.Email=email
        new_user.save()
        return redirect('home')
    return render(request,'signupxtra.html')
def ContactUs(request):
    return render(request, 'ContactUs.html')
def About(request):
    return render(request, 'About.html')
def Help(request):
    return render(request, 'Help.html')
def place_parcel(request):
    if request.method=='POST':
        # return render(request, 'Help.html')
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
        # User_Id =User.objects.get(id=request.user.id)
        neworder=Orders.objects.create(Order_Id=n,Order_Name=ordername,Parcel_Weight=weight,booked_date=Curr_datetime,From_House_No=houseno,From_Street=street,From_City=city, From_State=state,From_Pin_Code=pincode,Receiver_Name=receivername,To_House_No=houseno2,To_Street=street2,To_City=city2,To_State=state2,To_Pin_Code=pincode2,Order_Type=deliverymode)        
        neworder.save()
        return HttpResponse("saved.")
    return render(request, 'place_parcel.html')
def track_parcel(request):
    return render(request, 'parcel.html')
def estimate(request):
    return render(request, 'estimate.html')
