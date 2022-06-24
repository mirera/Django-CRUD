from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
class PostListView(ListView):
     model = Post

class PostCreateView(CreateView):
     model = Post
     fields = "__all__"
     success_url  = reverse_lazy("blog:all")

class PostDetailView(DetailView):
     model = Post
     fields = "__all__"
     success_url  = reverse_lazy("blog:all")

class PostUpdateView(UpdateView):
     model = Post
     fields = "__all__"
     success_url  = reverse_lazy("blog:all")
# this PostDeleteView check the success_url  = reverse_lazy(" ")

class PostDeleteView(DeleteView):
    model = Post
    success_url  = reverse_lazy("blog:all")