from django.urls import path
from customer.views import *

urlpatterns=[
    path('',CustHome.as_view(),name='ch'),
    path('pro/<int:pk>',ProductView.as_view(),name='pro'),
]