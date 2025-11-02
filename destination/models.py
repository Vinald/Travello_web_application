from django.db import models


# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="pictures")
    price = models.IntegerField(default=0)
    description = models.TextField()
    offer = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} {self.price} {self.description} {self.offer}'