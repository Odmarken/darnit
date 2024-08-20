from django.urls import path, re_path, include  
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('articles/', include('articles.urls')),  
    re_path(r'^about/$', views.about),  #
    path('', views.homepage),  
]
