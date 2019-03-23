from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Apply

class Date(forms.DateInput):
    input_type = 'date'

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserInformationUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email', )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('slug','user')
        widgets = {
            'birth_date':Date,
        }

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        exclude = ('time_stamp','qualifies','user')