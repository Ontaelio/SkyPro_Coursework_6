# Generated by Django 3.2.6 on 2022-12-20 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ad_images/', verbose_name='Картинка'),
        ),
    ]
