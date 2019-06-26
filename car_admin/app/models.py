from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=50,
                             verbose_name='Бренд')
    model = models.CharField(max_length=50,
                             verbose_name='Модель')

    def __str__(self):
        return f'{self.brand} {self.model}'

    def review_count(self):
        return Review.objects.filter(car=self).count()

    review_count.short_description = 'Количество статей'

    class Meta:
        verbose_name_plural = 'Автомобили'
        verbose_name = 'Автомобиль'
        ordering = ['-id']


class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE,
                            verbose_name='Автомобиль')
    title = models.CharField(max_length=100, verbose_name='Название статьи')
    text = models.TextField(verbose_name='Текст статьи')

    def __str__(self):
        return str(self.car) + ' ' + self.title

    class Meta:
        verbose_name_plural = 'Обзорные статьи'
        verbose_name = 'Обзорная статья'
