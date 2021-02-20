# Generated by Django 3.1.6 on 2021-02-20 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, max_length=100, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='username',
            field=models.CharField(db_index=True, max_length=100, null=True, unique=True, verbose_name='Никнейм'),
        ),
    ]
