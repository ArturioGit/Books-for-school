from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Назва')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    description = models.TextField(blank=True, verbose_name='Опис')
    group = models.ForeignKey('Group', on_delete=models.PROTECT, verbose_name='Клас')
    subject = models.ForeignKey('Subject', on_delete=models.PROTECT, verbose_name='Предмет')
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/", verbose_name='Обкладинка')
    pdf_file = models.FileField(upload_to="pdffiles/", null=True, verbose_name='PDF файл')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата змінення')
    is_published = models.BooleanField(default=True, verbose_name='Публікація')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('details', kwargs={'course_slug': self.slug})

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['group', 'title']


class Group(models.Model):
    number = models.IntegerField(verbose_name='Номер', unique=True, db_index=True)

    def __str__(self):
        return str(self.number)

    def get_absolute_url(self):
        return reverse('by_categories', kwargs={'subject_slug': 'all', 'group_number': self.number})

    class Meta:
        verbose_name = 'Клас'
        verbose_name_plural = 'Класи'
        ordering = ['-number']


class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name='Назва', unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('by_categories', kwargs={'subject_slug': self.slug, 'group_number': 0})

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предмети'
        ordering = ['name']
