# Generated by Django 3.2.6 on 2022-12-19 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_auto_20221219_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
