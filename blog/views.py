# blog/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Post
from django.shortcuts import render

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'content']

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'content']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

class AboutPageView(TemplateView):
    template_name = 'about.html'