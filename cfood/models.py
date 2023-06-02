from django.contrib.auth.models import User
from django.db import models
from autoslug import AutoSlugField
from django.shortcuts import reverse

# Create your models here.
class UserApp(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    name = models.CharField(max_length=70)


class Topic(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="title")

    def __str__(self):
        return self.title

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="title")
    image = models.CharField(max_length=400)
    description = models.TextField()
    ingredients = models.TextField()
    directions = models.TextField()
    servings = models.CharField(max_length=5)
    time = models.CharField(max_length=5)
    calories = models.CharField(max_length=5)
    fat = models.CharField(max_length=5)
    carbs = models.CharField(max_length=5)
    protein = models.CharField(max_length=5)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    favourites = models.ManyToManyField(
        User, related_name='favourite', default=None, blank=True)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse("detail", kwargs={
            "slug": self.slug,
        })

