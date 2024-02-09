from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Care_recipient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

class Care_giver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Image(models.Model):
    label = models.CharField(max_length=50, blank=False)
    image = models.ImageField(upload_to='library/')
    audio = models.FileField(upload_to='audio/', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    public = models.BooleanField(default=True)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, default='admin')

    def __str__(self):
        return self.label

class Board(models.Model):
    name = models.CharField(max_length=100)
    voice_choice = models.CharField(max_length=50, default="Jenny")
    def __str__(self):
        return self.name

class Tab(models.Model):
    name = models.CharField(max_length=50, null=False)
    images = models.ManyToManyField(Image)
    straps_num = models.IntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(5)])
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



