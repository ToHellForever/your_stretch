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


# модель для банеров в карусели (десктоп)
class Banner(models.Model):
    image = models.ImageField(upload_to='dekstop_banners/', verbose_name='Картинка')

    class Meta:
        verbose_name = 'Баннер (десктоп)'
        verbose_name_plural = 'Баннеры (десктоп)'

# модель для банеров в карусели (мобильные)
class MobileBanner(models.Model):
    image = models.ImageField(upload_to='mobile_banners/', verbose_name='Картинка')

    class Meta:
        verbose_name = 'Баннер (мобильный)'
        verbose_name_plural = 'Баннеры (мобильные)'
#  poetry run python manage.py makemigrations 
# модель для заказов натяжных потолков
class Order(models.Model):
    area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Площадь потолка (м²)')
    corners = models.IntegerField(verbose_name='Количество углов')
    lights = models.IntegerField(verbose_name='Количество светильников')
    pipes = models.IntegerField(verbose_name='Количество труб')
    ceiling_type = models.CharField(max_length=255, verbose_name='Тип потолка')
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_at']

    def __str__(self):
        return f"Заказ #{self.id} от {self.created_at.strftime('%d.%m.%Y %H:%M')}"

# модель для запросов обратного звонка
class CallbackRequest(models.Model):
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Запрос обратного звонка'
        verbose_name_plural = 'Запросы обратного звонка'
        ordering = ['-created_at']

    def __str__(self):
        return f"Запрос #{self.id} от {self.created_at.strftime('%d.%m.%Y %H:%M')} - {self.phone}"
