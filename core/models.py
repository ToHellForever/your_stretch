from django.db import models

# модель товара с полями: картинка, название, цена
class Product(models.Model):
    # картинка
    image = models.ImageField(upload_to='images/', verbose_name='Картинка')
    # название
    title = models.CharField(max_length=255, verbose_name='Название')
    # цена
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        
        
# примеры работ с полями: картинка, название, площадь, количество углов, профиль, цена
class Profile(models.Model):
    # картинка
    image = models.ImageField(upload_to='images/', verbose_name='Картинка')
    # название
    name = models.CharField(max_length=255, verbose_name='Название')
    # площадь
    area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Площадь')
    # количество углов
    angles = models.IntegerField(verbose_name='Количество углов')
    # профиль
    profile = models.CharField(max_length=255, verbose_name='Профиль')
    # цена
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    class Meta:
        verbose_name = 'Пример работы'
        verbose_name_plural = 'Примеры работ'


# галерея работ
class Gallery(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название галереи', blank=True, null=True)

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'

    def __str__(self):
        return self.name or f"Галерея {self.id}"

# фотографии в галерее
class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='images', verbose_name='Галерея')
    image = models.ImageField(upload_to='gallery_images/', verbose_name='Картинка')

    class Meta:
        verbose_name = 'Фотография галереи'
        verbose_name_plural = 'Фотографии галереи'


# модель для банеров в карусели
class Banner(models.Model):
    image = models.ImageField(upload_to='banners/', verbose_name='Картинка')
    
    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'
