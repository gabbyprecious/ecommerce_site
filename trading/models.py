from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products', default='python.png')
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

class Order(models.Model):
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    user = models.CharField(max_length=50)

    def __str__(self):
        return self.user
