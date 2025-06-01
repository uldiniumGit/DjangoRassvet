from django.db import models


class City(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='Название города')

    def __str__(self):
        return self.name


class Type(models.Model):
    type = models.CharField(max_length=32, unique=True, verbose_name='Тип')

    def __str__(self):
        return self.type


class Client(models.Model):
    name = models.CharField(max_length=32, verbose_name='Имя клиента')
    description = models.TextField(verbose_name='Описание')
    email = models.EmailField(max_length=32, unique=True, verbose_name='Email')

    def __str__(self):
        return self.name


class News(models.Model):
    news_name = models.CharField(max_length=32, verbose_name='Заголовок новости')
    news_text = models.TextField(verbose_name='Текст новости')

    def __str__(self):
        return self.news_name
