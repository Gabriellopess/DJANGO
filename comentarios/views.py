from django.shortcuts import render
from comentarios.models import Comentarios
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import generic

from comentarios.forms import ComentariosCreateForm
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ComentariosListView(ListView):
    model = Comentarios
    context_object_name = 'comentarios'
    template_name = 'comentarios/showComentarios.html'
    ordering = ['created_at',]

class ComentariosCreateView(LoginRequiredMixin, CreateView):
    model = Comentarios
    template_name = 'comentarios/createComentarios.html'
    form_class = ComentariosCreateForm
    success_url =  reverse_lazy('comentarios:showComentarios') #used for user pages redirection from CreatePosts to showPosts.


class ComentariosUpdateView(LoginRequiredMixin, UpdateView):
    model = Comentarios
    fields = {'comentario','post'}
    template_name = 'comentarios/update_comentarios.html'
    success_url = reverse_lazy('comentarios:showComentarios')

class ComentariosDeleteView(LoginRequiredMixin, DeleteView):
    model = Comentarios
    context_object_name = 'comentarios'
    template_name = 'comentarios/delete_comentarios.html'
    success_url = reverse_lazy('comentarios:showComentarios')