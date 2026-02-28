from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='luxurywatch/')
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "1. Yangi kalleksiyalar"

    def __str__(self):
        return self.title

class Banner(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='banners/')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "2. Bannerlar"

class Slider(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='sliders/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "3. Mahsulotlar"

    def __str__(self):
        return self.title