from django.utils import timezone
from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('черновик', 'Черновик'),
        ('опубликовано', 'Опубликовано'),
    )
    rubric = models.ForeignKey('Rubric', null=True,
    on_delete=models.PROTECT, verbose_name='Рубрика')
    title = models.CharField(max_length=250, verbose_name = 'Заголовок')
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    body = models.TextField(verbose_name='Текст')
    publish = models.DateTimeField(default=timezone.now, verbose_name='Публиковать')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=12,
                              choices=STATUS_CHOICES,
                              default='draft', verbose_name='Статус')
    class Meta:
        ordering = ('-publish',)
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])


    def __str__(self):
        return self.title

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']

    def __str__(self):
        return self.name
