from django.db import models

# Create your models here.


class Friend(models.Model):
    name = models.CharField(max_length=10)
    nickname = models.CharField(max_length=10)

    def __str__(self):
        return self.name