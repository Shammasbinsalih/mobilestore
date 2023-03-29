from django.urls import path
from .views import *

urlpatterns=[
    path('',StoreHome.as_view(),name='sh'),
    path('addpro/',AddProduct.as_view(),name='addp'),
    path('mypro/',MyProducts.as_view(),name='myp'),
    path('updatepro/<int:pk>/',UpdateProduct.as_view(),name='updatepro'),
]