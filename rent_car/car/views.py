from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from car.models import *
from django.urls import reverse
from car.form import UserRegistrationForm 
# Create your views here.

def admin_dashboard(request):
    total_users = User.objects.count()
    total_booking = Booking.objects.count()
    total_contact = Contact.objects.count()
    return render(request , 'Dashborad/index.html', {'total_users': total_users , 'total_bookings': total_booking , 'total_contact': total_contact})

def brandadd(request):
       if request.method == "POST":
        name = request.POST.get("name")
        brand = Brand( brand_name=name) 
        brand.save()
        return redirect("brandshow")
       else:
        pass 
       return render(request , "dashborad/brandadd.html")

def brandshow(request):
    brands = Brand.objects.all()
    brand={
        "brands":brands
    }
    return render(request , "dashborad/brandshow.html", brand)  

def brandedit(request, eid):
    brand = Brand.objects.get(id=eid)

    if request.method == "POST":
        name = request.POST.get("name")
        brand.brand_name = name
        brand.save()
        return redirect("brandshow")
    context = {
        "brand": brand
    }
    return render(request, 'dashborad/brandedit.html', context)
    
def branddelete(request, did):
    brand=Brand.objects.get(id=did)
    context={
        "brand":brand
    }
    if request.method == "POST":
        brand.delete()
        return redirect("brandshow")
    return render(request, 'dashborad/brandshow.html', context)

def Vehicleadd(request):
    brands = Brand.objects.all()
    brand={
        "brands":brands
    }
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("des")
        image = request.FILES.get("image")
        selected_brand_id = request.POST.get("brand_name")

        try:
            selected_brand = Brand.objects.get(pk=selected_brand_id)
        except Brand.DoesNotExist:
            return HttpResponse("Selected Brand does not exist.")

        vehicle = Vehicle(car_name=name, car_price=price, car_des=description, car_image=image, brand=selected_brand)
        vehicle.save()

        return redirect("vehicleshow")
    return render(request, "dashborad/Vehicleadd.html", brand)

def Vehicleshow(request):

    vehicles=Vehicle.objects.all()
    vehicle={
        "vehicles":vehicles
    }
    return render(request, "dashborad/Vehicleshow.html", vehicle)

def Vehicleedit(request ,eid):
    vehicle = Vehicle.objects.get(id=eid)
    brands = Brand.objects.all()
    
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("des")
        image = request.FILES.get("image")
        selected_brand_id = request.POST.get("brand_name")
        if name:
            vehicle.car_name = name
        if image:
             vehicle.car_image = image
        if selected_brand_id:
            try:
                selected_brand = Brand.objects.get(pk=selected_brand_id)
            except Brand.DoesNotExist:
                return HttpResponse("Selected category does not exist.")
            vehicle.brand = selected_brand
        if price:
            vehicle.car_price = price
        if description:
            vehicle.car_des = description
        vehicle.save()

        return redirect("vehicleshow")

    context = {
        "vehicle": vehicle,
        "brands": brands
    }
    return render(request, 'dashborad/Vehicleedit.html', context)

def Vehicledelete(request, did):
    vehicle = Vehicle.objects.get(id=did)
    if request.method == "POST":
        vehicle.delete()
        return redirect("vehicleshow")
    return render(request, 'dashborad/Vehicleshow.html', vehicle)

def bookingshow(request):
    bookings=Booking.objects.all()
    booking={
        "bookings": bookings
    }
    return render(request, 'dashborad/bookingshow.html', booking)


def bookingstatus(request, sid, status):
    booking =Booking.objects.get(id=sid)
    booking.status = status
    booking.save()
    return HttpResponseRedirect(reverse('bookingshow'))

def Testimonialshowing(request):
    testimonials=Testimonial.objects.all()
    testimonial={
        "testimonials":testimonials
    }
    return render(request, 'dashborad/testimonialshowing.html', testimonial)

def Testimonialstatus(request, tid, status):
    testimonial =Testimonial.objects.get(id=tid)
    testimonial.status = status
    testimonial.save()
    return HttpResponseRedirect(reverse('testimonialshowing'))

def contactshowing(request):
    contacts=Contact.objects.all()
    contact={
        'contacts':contacts
    }
    return render(request, 'dashborad/contactshowing.html',contact)

def userinfo(request):
    userinfo=User.objects.all()
    user={
        "userinfo":userinfo
    }
    return render(request, 'dashborad/userinfo.html',user)

def admin_profile(request):
    userinfo=Admin_user.objects.all()
    user={
        "userinfo":userinfo
    }
    return render(request, 'dashborad/admin_profile.html',user)

def usertotal(request):
    total_users = User.objects.count()
    return render(request, 'dashborad/try.html', {'total_users': total_users})

# dashboard register and login
def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        admin_user = Admin_user( admin_name=name, admin_email=email, admin_phone=phone, admin_password=password) 
        admin_user.save()
        return redirect("login")
    else:
        pass 
    return render(request, 'dashborad/register.html')

def login(request):
   
    return render(request, 'dashborad/login.html')




# wedsite register and login

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login or wherever appropriate after successful registration
            return redirect('user_login')
    else:
        form = UserRegistrationForm()
    return render(request, 'website/register.html', {'form': form})

def user_login(request):

    return render(request, "website/login.html")
# webiste

def index(request):
    vehicles=Vehicle.objects.all()
    testimonials=Testimonial.objects.all()
    vehicle={
        "vehicles":vehicles,
        "testimonials":testimonials
    }
    
    return render(request, 'website/index.html',vehicle)

def about(request):
    return render(request, "website/about.html")

def services(request):
    return render(request, "website/services.html")

def vehicle(request):
    return render(request, "website/vehicle.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        des = request.POST.get("des")
        contact = Contact( name=name, email=email, phone=phone, des=des) 
        contact.save()
        return redirect("contact")
    else:
        pass 
   
    return render(request,"website/contact.html")

def user_dashboard(request):
    return render(request, "user_dashboard/user_dashboard.html")

def user_test(request):
    return render(request, "user_dashboard/user_test.html")
  

def logout_view(request): 
    return render(request, "website/index.html")





def user_profile(request):
    userinfo=User.objects.all()
    user={
        "userinfo":userinfo
    }
    return render(request, 'user_dashboard/users_profile.html',user)

    
def bookingadd(request):
    vehicles=Vehicle.objects.all()
    vehicle={
        "vehicles":vehicles
    }
    if request.method == "POST":
        date = request.POST.get("date")
        selected_vehicle_id = request.POST.get("vehicle_name")

        try:
            selected_vehicle = Vehicle.objects.get(pk=selected_vehicle_id)
        except Vehicle.DoesNotExist:
            return HttpResponse("Selected vehicle does not exist.")

        booking = Booking(date=date, vehicle=selected_vehicle)
        booking.save()

        return redirect("bookinghistory")
    return render(request, 'user_dashboard/your_model_form.html', vehicle)

def bookinghistory(request):
    bookings=Booking.objects.all()
    booking={
        "bookings": bookings
    }
    return render(request, 'user_dashboard/booking_history.html', booking)


def Testimonialadd(request):
    users=User.objects.all()
    user={
        "users":users
    }
    if request.method == "POST":
        name = request.POST.get("name")
        des = request.POST.get("des")
        image = request.FILES.get("image")
        selected_users_id = request.POST.get("user_name")

        try:
            selected_users = User.objects.get(pk=selected_users_id)
        except User.DoesNotExist:
            return HttpResponse("Selected users does not exist.")

        testimonial = Testimonial(client_name=name,client_des=des,client_image=image, user=selected_users)
        testimonial.save()

        return redirect("testimonial")
    return render(request, 'user_dashboard/user_testimonial.html', user)

def Testimonialshow(request):
    testimonials=Testimonial.objects.all()
    testimonial={
        "testimonials":testimonials
    }
    return render(request, 'user_dashboard/testimonial.html', testimonial)

