from django.db import models


# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="pictures")
    price = models.IntegerField(default=0)
    description = models.TextField()
    offer = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.price} {self.description} {self.offer}"


class NewsPosts(models.Model):
    image = models.ImageField(upload_to="news_pictures")
    date = models.IntegerField()
    month = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f"{self.title} {self.date} {self.month} {self.category} {self.content}"


class Testimonial(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.author} {self.position} {self.content}"


class HomeSlider(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="home_slider_pictures")

    def __str__(self):
        return f"{self.title}"
