from django.db import models


class AnimalImage(models.Model):
    url = models.URLField()
    species = models.CharField(max_length=3)
    date = models.DateTimeField()
    type = models.CharField(max_length=4)

    def __str__(self):
        return f'{self.id}. {self.species}'
