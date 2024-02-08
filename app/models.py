from django.db import models

# Create your models here.

class SubProducts(models.Model):
    name = models.CharField(max_length = 50) 

    def __str__(self):
        return self.name    

class ProductDetails(models.Model):
        category = models.ForeignKey(SubProducts, on_delete=models.CASCADE)
        name = models.CharField(max_length = 50)
        size = models.CharField(max_length = 20)
        image = models.ImageField(upload_to='media/')

        def __str__(self):
            return self.name 