from django.db import models
from django.urls import reverse
from cloudinary.models import CloudinaryField

class News(models.Model):
    title = models.CharField('Sarlavha',max_length=150)
    date = models.DateField('Sana')
    text = models.TextField('Matn')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = CloudinaryField('image')

    def __str__(self):
        return self.title

class Events(models.Model):
    viloyat = models.CharField('Viloyat',max_length=150)
    city = models.CharField('Shahar/tuman',max_length=200)
    address = models.CharField('Manzil',max_length=150)
    phone = models.CharField('Telefon raqam',max_length=13)
    image = CloudinaryField('image')
    url = models.URLField('Telegram manzil')
    
    def __str__(self):
        return self.viloyat + '/' +self.city + '' + self.phone

class Location(models.Model):
    viloyat = models.CharField('Viloyat',max_length=150)

    def __str__(self):
        return self.viloyat

class City(models.Model):
    city = models.CharField('Shahar/tuman',max_length=150)

    def __str__(self):
        return self.city




class Contact(models.Model):
    name = models.CharField('F.I.O',max_length=150)
    address = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    phone = models.CharField('Telefon Raqam',max_length=13)
    image = CloudinaryField('image')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contact')