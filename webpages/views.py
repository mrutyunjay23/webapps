from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.


def home(request):
    return render(request, 'webpages/index.html')


def product(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'webpages/product.html',context)


def about(request):
    return render(request, 'webpages/about.html')


def services(request):
    return render(request, 'webpages/services.html')


def blog(request):
    all_blog = Blog.objects.all()
    context = {
        'all_blog': all_blog,
    }
    return render(request, 'webpages/blog.html', context)


def article(request, pk):
    blog_open = get_object_or_404(Blog, pk=pk)
    context = {
        'blog_open': blog_open
    }
    return render(request, 'webpages/article.html',context)


def contact(request):
    return render(request, 'webpages/contact.html')
