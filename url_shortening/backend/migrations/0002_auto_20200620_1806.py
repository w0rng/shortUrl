# Generated by Django 3.0.7 on 2020-06-20 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='short_link',
            field=models.SlugField(verbose_name='Сокращенная ссылка'),
        ),
    ]