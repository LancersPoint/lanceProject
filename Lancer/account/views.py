from django.shortcuts import render
from account.models import Profile
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistratioinForm, UserEditForm, ProfileEditForm
from django.contrib import messages
from django.core.mail import message, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .tokens import account_activation_token
from django.template.loader import render_to_string

def register(request):
    if request.method == 'POST':
        user_form = UserRegistratioinForm(request.POST, request.FILES)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Making the user to confirm mail
            new_user.is_active = False
            # Save the user object
            new_user.save()
            
            # GETTING THE USER INFO TO SAVE AS THE PROFILE
            country = user_form.cleaned_data['country']
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            photo = user_form.cleaned_data['photo']
            date_of_birth = user_form.cleaned_data['date_of_birth']
            title = user_form.cleaned_data['title']
            resume = user_form.cleaned_data['resume']
            phone_number = user_form.cleaned_data['phone_number']
            
            # saving info into the profile
            Profile.objects.create(user=new_user, country=country,
             photo=photo, phone_number=phone_number,
             resume=resume, title=title,date_of_birth=date_of_birth,
             )
            
            # Sending authentication/otp to user
            current_site = get_current_site(request)
            subject = 'Please Activate Your Account'
            # load a template like get_template() 
            # and calls its render() method immediately.
            message = render_to_string('activation_request.html', {
                'user': new_user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
                # method will generate a hash value with user related data
                'token': account_activation_token.make_token(new_user),
            })
            new_user.email_user(subject, message)
            # TODO: return redirect('activation_sent')
            # user = authenticate(username=username, password=password)
            # login(request, user)
            # TODO: return redirect("core:home")
        else:
            return render(request, 'account/register.html', {'form': user_form, 'error':user_form.errors})
            
    else:
        user_form = UserRegistratioinForm()
    # TODO return render(request, 'account/register.html',{'form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    # return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse("Invalid Login")
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})




@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(request, "Error while updating your profile")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})

