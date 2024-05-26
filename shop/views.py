from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    categories_with_products = []
    for cat in categories:
        cat_products = products.filter(category=cat)
        if cat_products.exists():
            categories_with_products.append((cat, cat_products))
    return render(request, 'shop/list.html', {'category': category, 'categories_with_products': categories_with_products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/detail.html', {'product': product})

