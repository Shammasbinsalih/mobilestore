from django.contrib import admin
from django.urls import path
from account.views import *
urlpatterns=[
    path('reg/',RegView.as_view(),name='reg'),
    path('',LogView.as_view(),name='log'),
]