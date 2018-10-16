from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.contrib import messages

def index(request):
    return render(request, 'user_example/index.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            #form.save()
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password1']
            # user = authenticate(uername=username, password=password)
            # login(request, user)
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            return redirect('index')
    else:
        form = UserCreationForm()

    form = UserCreationForm()
    context = {'form' : form}
    return render(request, 'registration/register.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'registration/change_password.html', {'form' : form})

