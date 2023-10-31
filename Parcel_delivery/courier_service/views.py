from datetime import datetime
from django.shortcuts import render,redirect,HttpResponse
from courier_service.models import user_details,Contacts,Orders,cities
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
citie={
    'Thiruvananthapuram':(8.52,76.94),
    'Chennai':(13.08,80.27),
    'Bengaluru':(12.97,77.59),
    'Hyderabad':(17.38,78.48),
    'Mumbai':(19.07,72.88),
    'Panaji':(15.29,74.12),
    'Bhopal':(23.26,77.41),
    'Amaravathi':(16.57,80.35),
    'Raipur':(21.27,81.86),
    'Bhubaneswar':(20.29,85.82),
    'Gandhinagar':(23.21,72.63),
    'Shimla':(31.10,77.26),
    'Chandigarh':(30.73,79.78),
    'Lucknow':(26.84,80.94),
    'Dehradun':(30.31,78.03),
    'Jaipur':(26.91,75.78),
    'Kolkata':(22.57,88.36),
    'Gangtok':(27.33,88.61),
    'Itanagar':(27.08,93.60),
    'Aizawl':(23.72,92.71),
    'Imphal':(24.81,93.93),
    'Agartala':(23.83,91.28),
    'Dispur':(26.14,91.77),
    'Kohima':(25.29,94.83),
    'Patna':(25.59,85.13),
    'Shillong':(25.27,91.77),
    'Amritsar':(31.55,74.34),
    'Ranchi':(23.34,85.31),
}
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
        
        if User.objects.filter(username=name).exists():
            messages.error(request,'This usename is already in use. Please use another one')
            return render(request,'signup.html')        
        if pas1!=pas2:
            messages.warning(request, 'password not same')
            return render(request, 'signup.html')       
        user=User.objects.create(username=name,password=make_password(pas1))
        user.save()
        user_det=user_details.objects.create(user=user,UserId=len(user_details.objects.all())+1)
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
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        mssg=Contacts.objects.create(name=name,email=email,message=message)
        mssg.save()
        messages.success(request, 'Your message has been delivered')
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
        User=user_details.objects.get(user=request.user)
        Userid=User.UserId
        neworder=Orders.objects.create(Order_Id=n,Order_Name=ordername,Parcel_Weight=weight,booked_date=Curr_datetime,From_House_No=houseno,From_Street=street,From_City=city, From_State=state,From_Pin_Code=pincode,Receiver_Name=receivername,To_House_No=houseno2,To_Street=street2,To_City=city2,To_State=state2,To_Pin_Code=pincode2,Order_Type=deliverymode,User_Id=Userid)        
        neworder.save()
        return HttpResponse("saved.")
    return render(request, 'place_parcel.html')
def track_parcel(request):
    if request.method=='POST':
        # return render(request, 'estimate.html')
        orderid=request.POST.get('orderid')
        #   order=Orders.objects.get(Order_Id=orderid)
        # status=order.Order_Status
        #   context={
        #       'status': status
        #   }
        try:
          order = Orders.objects.get(Order_Id=orderid)
          location=order.Order_location
          order_location = {
            "latitude": location.latitude,
            "longitude": location.longitude,
        }
        except Orders.DoesNotExist:
          order_location = None

        return render(request, 'track_parcel.html',{"order_location": order_location})
    return render(request, 'track_parcel.html')
def estimate(request):
    if request.method=='POST':
        city1=request.POST.get('to_city')
        city2=request.POST.get('from_city')
        weight=request.POST.get('weight')
        tod=request.POST.get('type')
        h=request.POST.get('height')
        l=request.POST.get('length')
        w=request.POST.get('width')
        l=int(l)
        w=int(w)
        h=int(h)
        vol=l*h*w
        cit1=cities.objects.filter(name=city1)[0]
        cit2=cities.objects.filter(name=city2)[0]
        lat1,long1=cit1.latitude,cit1.longitude
        lat2,long2=cit2.latitude,cit2.longitude
        dist=(lat1-lat2)**2+(long1-long2)**2
        dist=dist**(1/2)
        weight=int(weight)
        value=1
        # if tod=='Normal delivery':
        #     value=1 
        # elif tod=='Fast delivery':
        #     value=1.5 
        # elif tod=='Super fats delivery':
        #     value=2
        # else:
        #     value=2.5
        cost=(dist*58000+1500)*(vol*50)*weight*value
        time=int((dist*30+1)/value)
        context={'cost':cost,'time':time,}
        return render(request,'estimate.html',context)
    context={'cost':0.00,'time':2}
    return render(request, 'estimate.html',context)

def user_profile(request):
    User=user_details.objects.get(user=request.user)
    context={
        'city' : User.City,
        "userid" : User.UserId,
        'street' : User.Street,
        "state" : User.State,
        "Name" : User.user,
        "name" : User.user,
        "number" : User.Contact_Number,
        "mail" : User.Email,
        "h_no" : User.House_No,
        "state" : User.State,
        "pin" : User.Pin_Code,
    }
    return render(request, 'user_profile.html',context)
    
def edit(request):
    user_profile = user_details.objects.get(user=request.user)

    if request.method == 'POST':
        # Handle the form submission
        # user_profile.user = request.POST.get('name')
        user_profile.Email = request.POST.get('email', '')
        user_profile.Contact_Number = request.POST.get('number', '')
        user_profile.House_No = request.POST.get('h_no', '')
        user_profile.Street = request.POST.get('street', '')
        user_profile.City = request.POST.get('city', '')
        user_profile.State = request.POST.get('state', '')
        user_profile.Pin_Code = request.POST.get('pin', '')
        # Update other fields as needed
        user_profile.save()
        return redirect('user_profile')  # Redirect to the profile page after editing

    return render(request, 'edit_profile.html', {'user_profile': user_profile})