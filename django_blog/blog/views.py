from django.shortcuts import render, redirect 
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Profile

class Registration(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        new_email = request.POST.get('email')
        new_bio = request.POST.get('bio')
        new_picture = request.FILES.get('profile_picture')

        if new_email:
            request.user.email = new_email
            request.user.save()

        if new_bio:
            profile.bio = new_bio

        if new_picture:
            profile.profile_picture = new_picture

        profile.save()
        return redirect('profile') 

    context = {
        'profile': profile
    }
    return render(request, 'userprofile.html', context)




# Create your views here.
