from django.shortcuts import render , redirect

# Create your views here.
from .forms import SignupForm , UserForm , ProfileForm
from django.contrib.auth import authenticate, login
from .models import Profile
from django.urls import reverse


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # update the username and password 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username , password=password)
            # if user is valid in db .. login with it 
            login(request, user)
            # redirect to profile page  // not yet created profile 
            return redirect('/accounts/profile/')
    else:
        form = SignupForm()
    
    context = {
        'form': form

    }
    return render(request , 'registration/signup.html' , context)



def profile(request):
    # get the now profile for the now user
    profile = Profile.objects.get(user=request.user)
    context = {
        'profile': profile
    }
    return render(request , 'accounts/profile.html' , context)


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        userform = UserForm(request.POST, instance=request.user)
        profileform = ProfileForm(request.POST , request.FILES , instance=profile )

        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            # add user before save profile 
            myprofile.user = request.user
            myprofile.save() 
            return redirect(reverse('accounts:profile'))

        
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
    context = {
        'userform':userform,
        'profileform': profileform
    }
    return render(request , 'accounts/profile_edit.html' , context)
    