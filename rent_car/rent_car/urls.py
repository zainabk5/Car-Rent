"""
URL configuration for rent_car project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from car import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_dashboard',views.admin_dashboard, name='index'),
    path('brandshow',views.brandshow, name='brandshow'),
    path('brandadd', views.brandadd, name='brandadd'),
    path('brandedit/<eid>', views.brandedit, name="brandedit"),
    path('branddelete/<did>', views.branddelete, name="branddelete"),

    path('vehicleshow', views.Vehicleshow, name="vehicleshow"),
    path('vehicleadd/', views.Vehicleadd, name="vehicleadd"),
    path('vehicleedit/<eid>', views.Vehicleedit, name="vehicleedit"),
    path('vehicledelete/<did>', views.Vehicledelete, name="vehicledelete"),

    path('bookingshow', views.bookingshow , name="bookingshow"),
    path('bookingstatus/<int:sid>/<status>', views.bookingstatus, name='bookingstatus'),

    path('testimonialshowing',views.Testimonialshowing, name='testimonialshowing'),
    path('Testimonialstatus/<int:tid>/<status>', views.Testimonialstatus, name='Testimonialstatus'),

    path('contactshowing',views.contactshowing, name='contactshowing'),

    path('user',views.userinfo , name='user'),
    path('usertotal', views.usertotal, name='usertotal'),

    path('register',views.register , name='register'),
    path('login',views.login , name='login'),

    path('admin_profile',views.admin_profile, name='admin_profile'),


    # websit url 

    path('',views.index, name='index'),
    path('about',views.about, name='about'),
    path('services',views.services, name='services'),
    path('vehicle',views.vehicle, name='vehicle'),
    path('contact',views.contact, name='contact'),
    path('user_dashboard',views.user_dashboard, name='user_dashboard'),
    path('your_model/', views.bookingadd, name='your_model_view'),
    path('bookinghistory', views.bookinghistory, name='bookinghistory'),
    path('user_testimonial',views.Testimonialadd, name='user_testimonial'),
    path('testimonial',views.Testimonialshow, name='testimonial'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('user_register',views.user_register, name='user_register'),
    path('user_login',views.user_login, name='user_login'),
    path('user_profile',views.user_profile, name='user_profile'),
   


]
