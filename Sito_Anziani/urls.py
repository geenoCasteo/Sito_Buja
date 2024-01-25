from django.urls import path
from . import views
from .views import HomeView

urlpatterns = [
    #path('', views.index, name = "index"),
    path('about', views.about, name = "about"),
    path('', HomeView.as_view(), name = "index")
]
