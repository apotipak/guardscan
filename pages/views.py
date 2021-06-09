from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from pages.serializers import UserSerializer, GroupSerializer


def index(request):
    print("index")
    context = {}
    return render(request, 'index.html')
