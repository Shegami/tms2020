from django.db import models


class AnimalImage(models.Model):
    url = models.URLField()
    spicies = models.CharField(max_length=3)
    date = models.DateTimeField()
    type = models.CharField(max_length=4)
