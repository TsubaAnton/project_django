# Generated by Django 5.0.3 on 2024-04-15 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='current_version_indication',
            field=models.BooleanField(default=False, verbose_name='Признак текущей версии'),
        ),
    ]
