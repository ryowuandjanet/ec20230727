from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = (
    ('CR','三角台曆區'),
    ('ML','月曆區'),
    ('LS','年曆掛軸'),
    ('MS','中西式桌曆'),
    ('PN','工商手冊'),
    ('GH','日曆農民曆區'),
    ('CZ','便條盒區')
)

STATE_CHOICES =(
   ('Taipei','Taipei'),
   ('Taichaung','Taichaung'),
   ('Tainan','Tainan'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category=models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
      return self.title

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city=models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state=models.CharField(choices=STATE_CHOICES, max_length=100)

    def __str__(self):
      return self.name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
       return self.quantity * self.product.discounted_price