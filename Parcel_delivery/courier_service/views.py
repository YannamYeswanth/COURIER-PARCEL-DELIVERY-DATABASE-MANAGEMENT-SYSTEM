from datetime import datetime
from django.shortcuts import render,redirect,HttpResponse
from courier_service.models import user_details,Contacts,Orders,cities,Branches
from django.contrib.auth.models import User,Group
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import geopy.distance

# Create your views here.
def home(request):
    return render(request, 'Home.html')
def Login(request):

    context={'message':''}
    if request.method=='POST':
        name=request.POST.get('username')
        pas=request.POST.get('password')
        user=authenticate(username=name, password=pas)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            context['message']='Wrong Username or password'
            return render(request, 'login.html',context)
    return render(request,'login.html',context)
def signup(request):
      context={'message':''}
      if request.method=="POST":
        name=request.POST.get('username')
        pas1=request.POST.get('pas1')
        pas2=request.POST.get('pas2')
        if name=='' or pas1=='' or pas2=='':
            context['message']='Please fill out the credentials'
            return render(request,'signup.html',context)
        if User.objects.filter(username=name).exists():
            context['message']='This usename is already in use. Please use another one'
            return render(request,'signup.html',context)        
        if pas1!=pas2:
            context['message']='passwords are not same'
            return render(request, 'signup.html',context)       
        user=User.objects.create(username=name,password=make_password(pas1))
        user.save()
        user_det=user_details.objects.create(user=user,UserId=len(user_details.objects.all())+1)
        user_det.save()
        users=authenticate(username=name, password=pas1)
        if users is not None:
            login(request,users)
            return redirect('signupxtra')
      return render(request,'signup.html',context)
def signupxtra(request):
    if request.method=="POST":
        h_no=request.POST.get('H_No')
        street=request.POST.get('street')
        city=request.POST.get('city')
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')
        if pincode=='':
            pincode=0
        email=request.POST.get('email')
        contact=request.POST.get('c_no')
        if contact=='':
            contact=0
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
    places = Branches.objects.all()
    user = None

    if request.user.is_authenticated:
      user = user_details.objects.get(user=request.user)

      if request.method == 'POST':
        ordername = request.POST.get('ordername')
        weight = request.POST.get('weight')
        deliverymode = request.POST.get('deliverymode')
        receivername = request.POST.get('receivername')
        houseno = request.POST.get('houseno')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        houseno2 = request.POST.get('houseno2')
        street2 = request.POST.get('street2')
        city2 = request.POST.get('city2')
        state2 = request.POST.get('state2')
        pincode2 = request.POST.get('pincode2')
        ord_loc = cities.objects.filter(name=city2)[0]

        orders = Orders.objects.all()
        n = len(orders) + 1
        n+=26734595
        curr_datetime = datetime.now()
        user = user_details.objects.get(user=request.user)

        new_order = Orders.objects.create(
            Order_Id=n,
            Order_Name=ordername,
            Parcel_Weight=weight,
            booked_date=curr_datetime,
            From_House_No=houseno,
            From_Street=street,
            From_City=city,
            From_State=state,
            From_Pin_Code=pincode,
            Receiver_Name=receivername,
            To_House_No=houseno2,
            To_Street=street2,
            To_City=city2,
            To_State=state2,
            To_Pin_Code=pincode2,
            Order_Type=deliverymode,
            User_Id=user,
            Order_location=ord_loc
        )

        new_order.save()
        return HttpResponse("Saved.")

    context = {
        'places': places,
        # 'user': user,
    }

    return render(request, 'place_parcel.html', context)

def track_parcel(request):
    if request.method=='POST':
        # return render(request, 'estimate.html')
        
        orderid=request.POST.get('orderid')
        if orderid=="":
          order_location = None
          context={
              "order_location": order_location,
              "message" : "Enter valid order id."
          }
          return render(request, 'track_parcel.html',{})   
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
    order_location = None
    return render(request, 'track_parcel.html',{"order_location": order_location})
def estimate(request):
    places=Branches.objects.all()
    context={
        'cost':0,
        'time':2,
        'places':places,
        'message1':'',
        'message2':'',
        'message3':'',
    }
    if request.method=='POST':
        city1=request.POST.get('to_city')
        city2=request.POST.get('from_city')
        if city1=='0':
            context['message1']='Provide the city'
            return render(request,'estimate.html',context)
        if city2=='0':
            context['message2']='Provide the city'
            return render(request,'estimate.html',context)
        weight=request.POST.get('weight')
        tod=request.POST.get('deliverymode')
        h=request.POST.get('height')
        l=request.POST.get('length')
        w=request.POST.get('width')
        if h=='' or l=='' or w=='':
            context['message3']='Provide parcel details correctly'
            return render(request,'estimate.html',context)
        l=int(l)
        w=int(w)
        h=int(h)
        vol=l*h*w
        cit1=cities.objects.filter(name=city1)[0]
        cit2=cities.objects.filter(name=city2)[0]
        lat1,long1=cit1.latitude,cit1.longitude
        lat2,long2=cit2.latitude,cit2.longitude
        co1=(lat1,long1)
        co2=(lat2,long2)
        dist=geopy.distance.geodesic(co1,co2).km
        weight=int(weight)
        value=int(tod)
        cost=int(((dist*0.01+500)+(vol*0.0001))*weight*value)
        time=int((dist*0.01)/value)+1
        context['cost']=cost
        context['time']=time
        return render(request,'estimate.html',context)
    return render(request, 'estimate.html',context)

def user_profile(request):
    User=user_details.objects.get(user=request.user)
    orders = Orders.objects.filter(User_Id=User).order_by('booked_date')[:5]
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
        "orders" : orders
        
    }
    return render(request, 'user_profile.html',context)
    
def edit(request):
    user_profile = user_details.objects.get(user=request.user)
    orders = Orders.objects.filter(User_Id=user_profile).order_by('booked_date')[:5]
    context={
        'user_profile': user_profile,
        'orders' : orders
    }
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

    return render(request, 'edit_profile.html', context)

def my_orders(request):
    User=user_details.objects.get(user=request.user)
    orders = Orders.objects.filter(User_Id=User).order_by('booked_date')[:5]
    context={
        'orders' : orders
    }
    return render(request, 'my_orders.html',context)


# Check if the user is in the 'staff' group
def staff(request):
 user = request.user
 if user.is_staff:
    # User is in the 'staff' group
    # You can add your logic here for staff members
    return render(request, 'employee.html')
 else:
    # User is not in the 'staff' group
    # Handle this case as needed
    return render(request, 'Home.html')
