# COURIER/PARCEL DELIVERY DATABASE MANAGEMENT SYSTEM
 DBMS Project
# E Delivery - Courier Delivery System

## Motto
E Delivery aims to provide a seamless and reliable courier delivery experience, ensuring the safe and timely transport of parcels. Our platform prioritizes user convenience and transparency in delivery services.

## Project Objectives

E Delivery aims to revolutionize courier services by providing a seamless and user-friendly platform. Our project focuses on achieving the following objectives:

1. **Efficient Parcel Management:** Streamline the process of sending and receiving parcels with an efficient and organized management system.

2. **Real-time Parcel Tracking:** Implement a real-time tracking system to keep users informed about the status and location of their parcels.

3. **Estimation of Delivery price:** To let users know about the delivery charges before ordering.

4. **User Convenience:** Prioritize user convenience by offering a user-friendly interface, easy order placement, and accessible order history.

5. **Secure Packaging:** Ensure the safety of parcels during transit by providing secure packaging options to users.

6. **Flexible Delivery Options:** Cater to diverse user needs by offering various delivery modes, allowing users to choose the one that best suits their requirements.

7. **Reliable Order History:** Enable users to access and manage their order history, providing transparency and accountability in the delivery process.

E Delivery is committed to delivering a reliable and efficient courier management experience for our users.

---


## Features

### 1. User-friendly Interface
E Delivery offers an intuitive and easy-to-use interface, making it simple for users to place and track their orders.

### 2. Role based login system
E delivery has Role based login system where users, employees and admin can login with their respective login ids.

### 3. Real-time Tracking
Enjoy the convenience of real-time parcel tracking using our integrated maps feature. Keep tabs on your delivery every step of the way.

### 4. Estimation of Delivery Price
Users can know the delivery charges that would be applied for their parcel delivery.


### 5. Flexible Delivery Modes
Choose from a variety of delivery modes, including normal, fast, and more, tailored to your specific delivery needs.

### 6. Order History
Access your order history and keep track of your previous deliveries, providing a comprehensive overview of your E Delivery experience.


## Guidelines to Open the Website

Installation:
•	Install Python from [here](https://www.python.org/downloads/) manually.
•	Install project dependencies by running `py -m pip install -r requirements.txt`.
•	Install geopy distance by running `pip install geopy`.
•	Open a new terminal and Check if you are in Parcel_delivery folder. If not, run the command `cd Parcel_delivery` to open the folder
•	Run the commands `py manage.py makemigrations` and `py manage.py migrate`  in the project directory to make and apply migrations.
•	Create superuser with `py manage.py createsuperuser`. This step is optional.
•	Run the command `py manage.py runserver` to run the web server.
•	Open web browser and goto `127.0.0.1:8000` url to start using the web application.
•	For logging in as admin, you must have a superuser account. You can create super user using command `py manage.py createsuperuser` in the      terminal after opening Face_recognition folder(`cd Face_recognition`). We have already created a superuser. You can use that:
   Username: Edelivery
   Password: Edelivery 
•	For logging in as employee, you can know the employee ids and passwords in admin page if you login as admin.
•	For logging in as customer, you can create an account in sign up button.

