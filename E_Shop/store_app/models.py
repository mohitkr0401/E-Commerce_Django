from datetime import timezone
from idlelib.pyparse import trans
from django.utils import timezone

from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length= 200)
    def __str__(self): #to display the actual name on the screen
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self): #to display the actual name on the screen
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50)
    def __str__(self): #to display the actual name on the screen
        return self.name

class Filter_Price(models.Model):
    FILTER_PRICE = (
        ('1000 TO 10000','1000 TO 10000'),
        ('10000 TO 20000', '10000 TO 20000'),
        ('20000 TO 30000','20000 TO 30000'),
        ('30000 TO 40000', '30000 TO 40000'),
        ('40000 TO 50000', '40000 TO 50000'),
        ('50000 TO 60000','50000 TO 60000'),
        ('60000 TO 70000','60000 TO 70000'),
        ('70000 TO 80000','70000 TO 80000'),
        ('80000 TO 90000','80000 TO 90000'),
        ('90000 TO 100000','90000 TO 100000'),
        ('Above 100000','Above 100000')
    )
    price = models.CharField(choices=FILTER_PRICE, max_length=60)
    def __str__(self): #to display the actual name on the screen
        return self.price

class Product(models.Model):
    CONDITION = (('New','New'), ('Old','Old'))
    STOCK = ('IN STOCK', 'IN STOCK'),('OUT OF STOCK', 'OUT OF STOCK')
    STATUS = ('Publish', 'Publish'),('Draft','Draft')

    unique_id = models.CharField(max_length=200, unique=True, null=True,blank=True)
    image = models.ImageField(upload_to= 'Product_images/img')
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    condition = models.CharField(choices=CONDITION, max_length=100)
    information = models.TextField()
    description = models.TextField()
    stock = models.CharField(choices=STOCK, max_length=200)
    status = models.CharField(choices=STATUS, max_length=200)
    create_date = models.DateTimeField(default=timezone.now)

    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    filter_price = models.ForeignKey(Filter_Price,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.unique_id is None and self.create_date and self.id:
            self.unique_id=self.create_date.strftime('75%Y%m%d23') + str(self.id)
        return super().save(*args,**kwargs)

    def __str__(self): #to display the actual name on the screen
        return self.name


class Images(models.Model):
    image = models.ImageField(upload_to='Product_images/img')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)


class Tags(models.Model):
    name = models.CharField(max_length=200)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

