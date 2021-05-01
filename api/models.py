from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)
    image = models.TextField(max_length=10000, default='No data')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'Category id={self.id}, name={self.name}'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
        }


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=10000, default="No data")
    full = models.CharField(max_length=10000)
    price = models.IntegerField(default='No data')
    image = models.CharField(max_length=10000, default='No data')
    link = models.CharField(max_length=10000, default='No data')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
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
            'full': self.full,
            'price': self.price,
            'image': self.image,
            'link': self.link,
            'category': self.category_id,
        }