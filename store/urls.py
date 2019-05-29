from django.urls import path, include
from store.views import main_view, category_view, product_view

urlpatterns = [
    path('category/<category_slug>/', category_view, name='category_detail'),
    path('product/<product_slug>/', product_view, name='product_detail'),
    path('', main_view, name='base' ),
]