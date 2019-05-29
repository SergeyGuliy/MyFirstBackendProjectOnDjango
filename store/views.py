from django.shortcuts import render
from store.models import *
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
    context = {
        'parrentCategories': parrentCategories,
        'categories': categories
    }
    return render(request, 'main.html', context)


def product_view(request, product_slug):
    parrentCategories = ParentCategory.objects.all()
    categories = Category.objects.all
    product = Product.objects.get(slug=product_slug)
    context = {
        'product': product,
        'parrentCategories': parrentCategories,
        'categories': categories
    }
    return render(request, 'product.html', context)


def category_view(request, category_slug):
    parrentCategories = ParentCategory.objects.all()
    categories = Category.objects.all
    category = Category.objects.get(slug=category_slug)
    products_of_category = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products_of_category': products_of_category,
        'parrentCategories': parrentCategories,
        'categories': categories
    }
    return render(request, 'category.html', context)