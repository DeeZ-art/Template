# Generated by Django 4.0 on 2022-10-31 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_portfolio_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(upload_to='portfolio_images'),
        ),
    ]
