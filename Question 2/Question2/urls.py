from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from Answer2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('booking/', views.booking),
    url('cancel/', views.cancel),


]
