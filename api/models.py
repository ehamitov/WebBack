from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250)
    def to_json(self):
        return {
            'id' : self.id,
            'name' : self.name,

        }

class Product (models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=10000,default="No data")
    full = models.CharField(max_length=10000)
    price = models.IntegerField( default='No data')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    def __str__(self):
        return f'Product id={self.id}, name={self.name}'
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'full':self.full,
            'price': self.price,
            'category': self.category_id,
        }