from django.urls import path
from . import views
from .views import HomeView
from django.contrib import admin
from django.conf import settings  # new
from django.urls import path, include  # new
from django.conf.urls.static import static  # new

urlpatterns = [
    #path('', views.index, name = "index"),
    path('about', views.about, name = "about"),
    path('', HomeView.as_view(), name = "index")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
