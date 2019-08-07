# This file means the programming logic of our project. Where we send and connect the
# data in database to the .html file.

from django.shortcuts import render
from posts.models import post
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import generic

from posts.forms import PostCreateForm
from django.urls import reverse_lazy

# Create your views here.

class PostListView(ListView):
    model = post
    context_object_name = 'posts'
    template_name = 'posts/showPosts.html'
    ordering = ['-created_at',]

class PostCreateView(CreateView):
    model = post
    template_name = 'posts/createposts.html'
    form_class = PostCreateForm
    success_url =  reverse_lazy('posts:showPosts') #used for user pages redirection from CreatePosts to showPosts.


class PostUpdateView(UpdateView):
    model = post
    fields = {'autor','texto'}
    template_name = 'posts/list.html'
    success_url = reverse_lazy('posts:showPosts')

class PostDeleteView(DeleteView):
    model = post
    context_object_name = 'post'
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('posts:showPosts')




