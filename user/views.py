from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm


def login(request):
    form = UserForm(request.POST or None)