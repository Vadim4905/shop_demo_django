from django.db import models

# Create your models here.

# Product (Продукт)
#  • Назва продукту (name): CharField
#  • Опис продукту (description): TextField
#  • Ціна (price): DecimalField
#   Review (Відгук)
#  • Продукт (product): ForeignKey до Product
#  • Автор (author): CharField
#  • Текст відгуку (text): TextField
#  • Рейтинг (rating): IntegerField
 
 
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=6)
    
class Review(models.Model):
    product = models.ForeignKey(Product,related_name='reviews',on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField()
    