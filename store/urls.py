from django.urls import path, include
from store.views import main_view, category_view, product_view, parent_category_view, cart_view, add_to_cart_view

urlpatterns = [
    path('category/<category_slug>/', category_view, name='category_detail'),
    path('product/<product_slug>/', product_view, name='product_detail'),
    path('', main_view, name='base' ),
    path('<parent_category_slug>', parent_category_view, name='parent_category_detail'),
    path('cart/', cart_view, name='cart'),
    path('add_to_cart/<product_slug>', add_to_cart_view, name='add_to_cart')
]