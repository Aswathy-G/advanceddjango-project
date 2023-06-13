from django.db import models

from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "categories"

    def __str__ (self):
        return self.title

class Product(models.Model):
    image = models.ImageField(upload_to="products/images")
    title = models.CharField(max_length=255)
    categories = models.ManyToManyField("web.category")
    description = models.TextField()
    price = models.CharField(max_length=255)

    is_deleted = models.BooleanField(default = False)
    is_edit = models.BooleanField(default = False)
    
    

    def __str__ (self):
        return self.title
