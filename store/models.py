from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from transliterate import translit
from django.urls import reverse


# Creating functions for models
def image_folder(instanse, fileName):
    fileName = instanse.slug + '.' + fileName.split('.')[1]
    return "{0}/{1}".format(instanse.slug, fileName)


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ParentCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('parent_category_detail', kwargs={'parent_category_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)
    parentCategory = models.ForeignKey(ParentCategory, on_delete=models.CASCADE, default=None, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'category_slug': self.slug})


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)
    description = models.TextField(default= 'НАПИШИТЕ ОПИСАНИЕ ПРОДУКТА!')
    image = models.ImageField(upload_to= image_folder, blank=True)
    warranty = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    avaliable =models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_slug': self.slug})


def pre_save_category_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(str(instance.name), reversed=True))
        instance.slug = slug


pre_save.connect(pre_save_category_slug, sender=ParentCategory)
pre_save.connect(pre_save_category_slug, sender=Category)
pre_save.connect(pre_save_category_slug, sender=Product)






