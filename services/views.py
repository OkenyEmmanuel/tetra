from django.shortcuts import render
from services.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from providers.models import ClientAppointment
# Create your views here.
def index(request):
    return render(request, 'base.html')

def register(request):
     registered = False
     
     if request.method == 'POST':
         user_form = UserForm(data=request.POST)
         profile_form = UserProfileInfoForm(data=request.POST)
         
         if user_form.is_valid() and profile_form.is_valid():
             user = user_form.save()
             user.save()
             
             profile = profile_form.save(commit=False)
             profile.user = user
             profile.save()
             
             registered = True
         else:
            print(user_form.errors, profile_form.errors)
     else:
         user_form = UserForm()
         profile_form = UserProfileInfoForm()
         
     return render(request, 'services/registeration.html',{
        'registered':registered,
        'user_form':user_form,
        'profile_form':profile_form
    })
     
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')     
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('ACCOUNT IS DEACTIVATED')
        else:
            return HttpResponse("Please use correct id and password")  
        
    return render(request, 'services/login.html')  
         
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))            

def registers(request):
    if request.method == "POST":
        firstname =request.POST['username']
        lastname =request.POST['lastname']
        email = request.POST['email'] 
        tel =request.POST['tel']
        gen = request.POST['gender']
        dob = request.POST['dob']
        address = request.POST['address']
        date = request.POST['dob1']
        time = request.POST['dob3']
        reason = request.POST['appointment']
        
        obj=ClientAppointment()
        obj.firstname=firstname
        obj.lastname=lastname
        obj.email=email
        obj.telephone=tel
        obj.gender=gen
        obj.dob = dob
        obj.address = address
        obj.date_of_appointment = date
        obj.time_of_appointment = time
        obj.reason = reason
        obj.save()
        return HttpResponse("<h2> Your Appointment Has Been Recorded Successfully</h2>")
    return render(request, 'regist.html')

            
def third_view(request):
    return render(request, 'third.html') 

            
def second_view(request):
    return render(request, 'second.html') 

     
        