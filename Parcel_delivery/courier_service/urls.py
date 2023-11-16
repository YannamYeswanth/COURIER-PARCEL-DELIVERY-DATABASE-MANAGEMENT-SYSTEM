from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('Home', views.home, name='home'),
    path('login',views.Login,name='login'),
    path('signup',views.signup,name='signup'),
    path('signupxtra',views.signupxtra,name='signupxtra'),
    path('About', views.About, name='About'),
    path('ContactUs', views.ContactUs, name='ContactUs'),
    path('Help', views.Help, name='Help'),
    path('place_parcel', views.place_parcel, name='place_parcel'),
    path('track_parcel', views.track_parcel, name='track_parcel'),
    path('estimate', views.estimate, name='estimate'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('edit', views.edit, name='edit'),
    path('my_orders', views.my_orders, name='my_orders'),
    path('staff', views.staff, name='staff'),
    path('edit_orders', views.edit_orders, name='edit_orders'),
    path('add_employee', views.add_employee, name='add_employee'), 
    path('admin', views.admin, name='admin'),
    path('add_branch', views.add_branch, name='add_branch'),
    path('add_department', views.add_department, name='add_department'),
    path('add_city', views.add_city, name='add_city'),
    path('emp_details', views.emp_details, name='emp_details'),
    path('branch_details', views.branch_details, name='branch_details'),
    path('dept_details', views.dept_details, name='dept_details'),
    path('cities_details', views.cities_details, name='city_details'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
