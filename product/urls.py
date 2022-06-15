from django.urls import path
from product import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('product-a', views.add_product, name='add_product_a')
]