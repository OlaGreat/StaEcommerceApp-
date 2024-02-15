from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=14)
    delivery_Address = models.TextField()

    def __str__(self) -> str:
        return f" {self.first_name} {self.last_name}"
    
class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = 'categories'


class Product(models.Model):
    name = models.CharField(max_length=50)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)   
    image = models.ImageField(upload_to='upload/media/')
    description = models.TextField()
    price = models.DecimalField(max_digit=2, decimal_places=2)
    discount_price = models.DecimalField(max_digit=2,decimal_places=2)

    def __str__(self):
        return f'{self.name}'
    


    
class vendor(models.Model):
    vendor_full_name = models.CharField(max_length=150)
    store_name = models.TextField()
    product_type = models.CharField(max_length = 100)



