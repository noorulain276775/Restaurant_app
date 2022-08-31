from django.urls import path
from .views import *

urlpatterns =[
    path('', HomeView.as_view(), name="home"),
    path('login', LoginView.as_view(), name="login"),
    path('register', RegisterView.as_view(), name="register"),
    path('menu', MenuView.as_view(), name="menu"),
    path('cart', CartView.as_view(), name="cart"),
    path('cart/<int:id>', CartView.as_view(), name="delete_cart"),
    path('order', OrderCreationView.as_view(), name="order"),
    path('orders', OrderView.as_view(), name="order_view"),
    path('logout', logout_view, name="logout"),
]
