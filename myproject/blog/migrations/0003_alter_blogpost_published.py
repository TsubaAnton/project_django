# Generated by Django 5.0.3 on 2024-04-13 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogpost_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Признак публикации'),
        ),
    ]
