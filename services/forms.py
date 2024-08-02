from django import forms
from django.contrib.auth.models import User
from services.models import user_profile
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
        
        labels = {
            'password1':'password',
            'password2': 'Confirm Password'
        }
class UserProfileInfoForm(forms.ModelForm):
    bio = forms.CharField(required=False)
    service_subscriber = 'service_subscriber'
    service_user  = 'service_user'
    service_provider = 'service_provider' 
    user_types = [
        ( service_subscriber,'service_subscriber'),
        (service_user, 'service_user')
    ]   
    user_type = forms.ChoiceField(required=True, choices=user_types)
    
    class Meta():
        model = user_profile
        fields = ('bio','profile_Pic','user_type')   
        