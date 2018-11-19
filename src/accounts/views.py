from datetime import datetime
from django.utils import timezone

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from accounts.forms import UserForm, UserLoginForm
from accounts.models import User


def login_view(request):  # users will login with their Email & Password
    if request.user.is_authenticated:
        return redirect("/")
    else:
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            # authenticate with Email & Password
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect("/")
        else:
            print(form.errors)
        return render(request, "accounts/login.html", {})


def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        errors = {}
        gender = request.POST.get('gender')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        age = request.POST.get('age')
        if password != confirm_password:
            errors["password"] = "Password should be matched"
            return render(request, 'accounts/register.html', errors)
        else:
            form = UserForm(request.POST or None)
            if form.is_valid():
                user = form.save(commit=False)
                password = form.cleaned_data.get("password1")
                user.set_password(password)
                user.save()
                return redirect('/')
            else:
                print(form.errors)
        return render(request, 'accounts/register.html')
    return render(request, 'accounts/register.html')


def logout_view(request):  # logs out the logged in users
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        user = get_object_or_404(User, email=request.user.email)
        user.updated_at = datetime.now(tz=timezone.utc)
        user.save()
        logout(request)
        return redirect("/")


@login_required(login_url="/login")
def update_profile(request):
    context = {
        "user": request.user
    }
    if request.method == "GET":
        return render(request, "profile/edit.html", context)
    else:
        about = request.POST['description']
        looking_for = request.POST['looking_for']
        interests = request.POST['interests']
        city = request.POST['city']
        country = request.POST['country']
        user = get_object_or_404(User, email=request.user.email)
        user.about = about
        user.looking_for = looking_for
        user.interests = interests
        user.city = city
        user.country = country
        user.save()
        return redirect('/profile/edit')


@login_required(login_url="/login")
def upload_profile_picture(request):
    photo = request.FILES['photo']
    user = get_object_or_404(User, email=request.user.email)
    user.profile_picture = photo
    user.save()
    return redirect('/profile/edit')
