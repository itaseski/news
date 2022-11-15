# Generated by Django 4.1.3 on 2022-11-14 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=64, unique=True, verbose_name='Назив')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['title'],
            },
        ),
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Креирано'),
        ),
        migrations.AlterField(
            model_name='news',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Дали е публикувано'),
        ),
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотографија'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=64, verbose_name='Назив'),
        ),
        migrations.AlterField(
            model_name='news',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Поправено'),
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='news.category'),
        ),
    ]