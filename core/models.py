from django.db import models

# модель товара с полями: картинка, название, цена
class Product(models.Model):
    # картинка
    image = models.ImageField(upload_to='images/')
    # название
    title = models.CharField(max_length=255)
    # цена
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        
        
# примеры работ с полями: картинка, название, площадь, количество углов, профиль, цена 
class Profile(models.Model):
    # картинка
    image = models.ImageField(upload_to='images/')
    # название
    name = models.CharField(max_length=255)
    # площадь
    area = models.DecimalField(max_digits=10, decimal_places=2)
    # количество углов
    angles = models.IntegerField()
    # профиль
    profile = models.CharField(max_length=255)
    # цена
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Пример работы'
        verbose_name_plural = 'Примеры работ'


# галерея работ с полями: картинка
class Gallery(models.Model):
    # картинка
    image = models.ImageField(upload_to='images/')
    
    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'