from django.shortcuts import render

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
    return render(request, 'place_parcel.html')
def track_parcel(request):
    return render(request, 'parcel.html')
def estimate(request):
    return render(request, 'estimate.html')
