from django.shortcuts import render
from categoria.models import Categoria
from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from categoria.forms import CategoriaCreateForm
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    template_name = 'categoria/createcategoria.html'
    form_class = CategoriaCreateForm
    success_url = reverse_lazy('posts:showPosts')

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    fields = {'categoria'}
    template_name = 'categoria/updatecategoria.html'
    success_url = reverse_lazy('posts:showPosts')


class CategoryListView(ListView):
    model = Categoria
    context_object_name = 'categoria'
    template_name = 'categoria/showCategories.html'
    ordering = ['-created_at',]
 

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    context_object_name = 'categoria'
    template_name = 'categoria/deletecategories.html'
    success_url = reverse_lazy('categoria:showCategories')

