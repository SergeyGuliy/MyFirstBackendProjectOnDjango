from django.db import models

# Creating functions for models
def image_folder(instanse, fileName):
    fileName = instanse.slug + '.' + fileName.split('.')[1]
    return "{0}/{1}".format(instanse.slug, fileName)


# Create your models here.
class ParentCategory(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField()
    def __str__(self):
        return self.name

class Category(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField()
    parentCategory = models.ForeignKey(ParentCategory, on_delete=models.CASCADE, default=None )
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,)
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    description = models.TextField(default= 'НАПИШИТЕ ОПИСАНИЕ ПРОДУКТА!')
    image = models.ImageField(upload_to= image_folder, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    avaliable =models.BooleanField(default=True)

    def __str__(self):
        return self.title

