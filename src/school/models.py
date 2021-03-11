from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.pk}. {self.name}'


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    group = models.ForeignKey(
        Group,
        null=True,
        on_delete=models.CASCADE,
        related_name='students',
    )

    def __str__(self):
        return f'{self.pk}. '\
               f'{self.first_name} '\
               f'{self.last_name} '\
               f'{self.group.name}'
