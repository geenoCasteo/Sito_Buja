from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.
# def index(request):
#     return render(request, "index.html", {})

def about(request):
    return render(request, "about.html", {})

class HomeView(ListView):
    model = Post
    template_name = "index.html"
