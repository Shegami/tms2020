from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=20)
    price = models.FloatField()
    quantity = models.IntegerField()
    comment = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id}. {self.title} - ' \
               f'${self.price} - q-ty: {self.quantity}'
