from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=64, db_index=True, unique=True, verbose_name='Назив')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']

class News(models.Model):
    title = models.CharField(max_length=64, verbose_name='Назив')
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Креирано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Поправено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотографија')
    is_published = models.BooleanField(default=True, verbose_name='Дали е публикувано')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-created_at']




