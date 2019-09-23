from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<book_id>', views.cart_add, name='cart_add'),
    path('remove/<book_id>', views.cart_remove, name='cart_remove'),
]