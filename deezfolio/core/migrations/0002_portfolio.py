# Generated by Django 4.0 on 2022-10-30 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='portfolio_images')),
                ('heading', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
