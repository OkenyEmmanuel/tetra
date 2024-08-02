from django.shortcuts import render
from .models import Department, Department_Details, Doctor, ClientAppointment
from django.views.generic import (TemplateView, DetailView, ListView, FormView)
from django.utils import timezone
from django.http import HttpResponse
from datetime import timedelta
from .forms import RegistrationForm  # Import the RegistrationForm

# Create your views here.
class ServiceListView(ListView):
    context_object_name = 'services'
    model = Department
    template_name = 'providers/servicelistview.html'
     
class CategoryListView(DetailView):
    context_object_name = 'services'
    model = Department
    template_name = 'providers/category_list_view.html'
    
class DescriptionListView(DetailView):
    context_object_name = 'descriptions'
    model = Department_Details
    template_name = 'providers/description_list_view.html'    

def registers(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)  # Initialize the form with POST data
        if form.is_valid():  # Check if form is valid
            cleaned_data = form.cleaned_data  # Access cleaned form data
            dob = cleaned_data['dob']
            appointment_date = cleaned_data['dob1']

            # Check if date of birth is greater than 20 years from today
            if timezone.now() - dob < timedelta(days=365*20):
                return HttpResponse("<h2>Date of birth must be greater than 20 years from today</h2>")

            # Check if appointment date is a day greater than today
            if appointment_date <= timezone.now() + timedelta(days=1):
                return HttpResponse("<h2>Appointment date must be a day greater than today</h2>")

            # If all validations pass, save the form data to the database
            form.save()

            return HttpResponse("<h2>Thank you For Registering With Jonjo Fashions</h2>")  
    else:
        form = RegistrationForm()  # If it's a GET request, create an empty form

    return render(request, 'regist.html', {'form': form})  # Pass the form to the template

def third_view(request):
    return render(request, 'third.html')
