from django.contrib import admin
from django.urls import path
from Answer1 import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url('items/',views.items),

]
