"""
Definition of models.
"""

from django.db import models
from django.contrib import admin
from datetime import datetime
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

#модель данных блога
class Blog(models.Model):
     title = models.CharField(max_length = 100, unique_for_date = "posted", verbose_name = "Заголовок")
     author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Автор")
     description = models.TextField(verbose_name = "Краткое содержание")
     content = models.TextField(verbose_name = "Полное содержание")
     posted = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Опубликована")
     image = models.FileField(default = 'temp.jpg', verbose_name = "Путь к изображению")
     def get_absolute_url(self): # метод возвращает строку с URL-адресом записи
         return reverse("blogpost", args=[str(self.id)])

     def __str__(self): # метод возвращает название, используемое для представления отдельных записей в административном разделе
         return self.title
     class Meta:
         db_table = "Posts" # имя таблицы для модели
         ordering = ["-posted"] # порядок сортировки данных в модели ("-" означает по убыванию)
         verbose_name = "статья блога" # имя, под которым модель будет отображаться в административном разделе (для одной статьи блога)
         verbose_name_plural = "статьи блога" # тоже для всех статей блога


admin.site.register(Blog)

class Comment(models.Model):
    text = models.TextField(verbose_name = "Комментарий")
    date = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Дата")
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор")
    post = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name = "Статья")
    
    def __str__(self): # метод возвращает название, используемое для представления отдельных записей в административном разделе
        return 'Комментарий %s к %s' % (self.author, self.post)
    
    class Meta:
        db_table = "Comments" # имя таблицы для модели
        verbose_name = "Комментарий" # имя, под которым модель будет отображаться в административном разделе (для одной статьи блога)
        verbose_name_plural = "Комментарии к статьям блога" # тоже для всех статей блога
        ordering = ["-date"] # порядок сортировки данных в модели ("-" означает по убыванию)

admin.site.register(Comment)


class Products(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Название")
    description = models.TextField(verbose_name = "Описание")
    price = models.CharField(max_length = 100, verbose_name = "Цена")
    image = models.FileField(default = 'temp.jpg', verbose_name = "Путь к картинке")


    def __str__(self): # метод возвращает название, используемое для представления отдельных записей в административном разделе
        return self.title

    class Meta:
        db_table = "Products" # имя таблицы для модели
        ordering = ["title"] # порядок сортировки данных в модели ("-" означает по убыванию)
        verbose_name = "Товар" # имя, под которым модель будет отображаться в административном разделе (для одной статьи блога)
        verbose_name_plural = "Товар" # тоже для всех статей блога

admin.site.register(Products)

class Orders(models.Model):
    date = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Дата")
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Клиент")
    post = models.ForeignKey(Products, on_delete = models.CASCADE, verbose_name = "Товар")
    ready = models.BooleanField(default = False, verbose_name = "Статус")
    
    def __str__(self): # метод возвращает название, используемое для представления отдельных записей в административном разделе
        return 'Заказ от %s  %s' % (self.author, self.post)
    
    class Meta:
        db_table = "Orders" # имя таблицы для модели
        verbose_name = "Заказ" # имя, под которым модель будет отображаться в административном разделе (для одной статьи блога)
        verbose_name_plural = "Заказ" # тоже для всех статей блога
        ordering = ["-id"] # порядок сортировки данных в модели ("-" означает по убыванию)

admin.site.register(Orders)
