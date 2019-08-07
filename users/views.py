from django.shortcuts import render
from users.models import User
from django.views.generic import ListView
from django.views import generic

# Create your views here.

class UserListView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'users/list.html'
