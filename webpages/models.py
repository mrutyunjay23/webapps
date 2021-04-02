from django.db import models
from ckeditor.fields import RichTextField
from djmoney.models.fields import MoneyField


# Create your models here.

class Blog(models.Model):
    title = models.TextField(max_length=30)
    blog_text = RichTextField(null=True)
    image = models.ImageField(upload_to='blog_images/%Y/%m/', null=True)
    date = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    p_name = models.CharField(max_length=55)
    p_description = RichTextField(null=True)
    p_image = models.ImageField(upload_to='media/product_image/%Y/%m/', null=True)
    p_price = MoneyField(decimal_places=2, max_digits=8, default_currency='INR')

    def __str__(self):
        return self.p_name


class company(models.Model):
    name = models.CharField(max_length=50)
    about = RichTextField()
    for_contact = RichTextField()
