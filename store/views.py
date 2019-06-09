from django.shortcuts import render
from store.models import *
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
# Create your views here.


# def base_view(request):
#     parrentCategories = ParentCategory.objects.all()
#     categories = Category.objects.all()
#     context = {
#         'parrentCategories': parrentCategories,
#         'categories': categories
#     }
#     return render(request, 'base.html', context)



def main_view(request):
    parrentCategories = ParentCategory.objects.all()
    categories = Category.objects.all
    cart =Cart.objects.first()
    context = {
        'parrentCategories': parrentCategories,
        'categories': categories,
        'cart': cart
    }
    return render(request, 'main.html', context)


def product_view(request, product_slug):
    parrentCategories = ParentCategory.objects.all()
    categories = Category.objects.all
    cart = Cart.objects.first()
    product = Product.objects.get(slug=product_slug)
    context = {
        'product': product,
        'parrentCategories': parrentCategories,
        'categories': categories,
        'cart': cart
    }
    return render(request, 'product.html', context)


def category_view(request, category_slug):
    parrentCategories = ParentCategory.objects.all()
    categories = Category.objects.all
    cart = Cart.objects.first()
    category = Category.objects.get(slug=category_slug)
    products_of_category = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products_of_category': products_of_category,
        'parrentCategories': parrentCategories,
        'categories': categories,
        'cart': cart
    }
    return render(request, 'category.html', context)


def parent_category_view(request, parent_category_slug):
    parrentCategories = ParentCategory.objects.all()
    categories = Category.objects.all
    cart = Cart.objects.first()
    parrentCategory = ParentCategory.objects.get(slug=parent_category_slug)
    context = {
        'parrentCategories': parrentCategories,
        'categories': categories,
        'parrentCategory': parrentCategory,
        'cart': cart
    }
    return render(request, 'parrentCategory.html', context)


def cart_view(request):
    parrentCategories = ParentCategory.objects.all()
    categories = Category.objects.all()
    cart = Cart.objects.first()
    context ={
        'parrentCategories': parrentCategories,
        'categories': categories,
        'cart': cart
    }
    return render(request, 'cart.html', context)


def add_to_cart_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    new_item, _ = CartItem.objects.get_or_create(product=product, item_total_price=product.price)
    cart = Cart.objects.first()
    if new_item not in cart.items.all():
        cart.items.add(new_item)
        cart.save()
        return HttpResponseRedirect('/cart/')