from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=20, blank=True)
    state = models.CharField(max_length=15, blank=True)
    country = models.CharField(max_length=20, blank=True)
    postal_code = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return self.user.username
    
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)
    






# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=14)
    delivery_Address = models.TextField()
    password = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f" {self.first_name} {self.last_name}"
    


    
class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'





class Product(models.Model):
    name = models.CharField(max_length=50)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)   
    image = models.ImageField(upload_to='upload/product/')
    description = models.TextField()
    price = models.DecimalField(default=0, max_digits=7, decimal_places=2)
    discount_price = models.DecimalField(default=0, max_digits=7, decimal_places=2, blank=True)

    def __str__(self):
        return self.name
    


    

class Order(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    orderNumber = models.ImageField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)
    address = models.TextField()
    phone = models.CharField(max_length=14)
    status = models.BooleanField(default = False)
    date = models.DateTimeField(default = datetime.today)

    def __str__(self):
        return self.orderNumber

    


    
class vendor(models.Model):
    vendor_full_name = models.CharField(max_length=150)
    store_name = models.TextField()
    product_type = models.CharField(max_length = 100)

    def __str__(self):
        return self.vendor_full_name


