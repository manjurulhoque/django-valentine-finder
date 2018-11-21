from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from src.accounts.forms import UserForm


@api_view(['POST'])
def register(request):
    errors = {}
    gender = request.POST.get('gender')
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')
    age = request.POST.get('age')
    if password != confirm_password:
        errors["password"] = "Password should be matched"
        return Response(errors)
    else:
        form = UserForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            return Response({'success': 'Registration success', 'status': status.HTTP_200_OK})
        else:
            print(form.errors)
            return Response({'error': form.errors, 'status': status.HTTP_400_BAD_REQUEST})
