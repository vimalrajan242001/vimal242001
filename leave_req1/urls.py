
from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.contrib import admin
from leave_req1.forms import  leave_request_form

urlpatterns = [
    path('leave_req1', views.leave_req1, name='leave_req1'),
        path('homes', views.homes, name='homes'),
]