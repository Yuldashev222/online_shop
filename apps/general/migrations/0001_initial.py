# Generated by Django 5.0.3 on 2024-04-01 09:15

import apps.general.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='general/image')),
                ('title', models.CharField(max_length=35)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('amount', models.DecimalField(decimal_places=1, help_text='So`mda yoki foizda kiriting!', max_digits=10)),
                ('amount_is_percent', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_price', models.PositiveIntegerField(help_text='So`mda kiriting!')),
                ('store_name', models.CharField(max_length=30)),
                ('logo', models.ImageField(upload_to='image/%Y/%m/%d/')),
                ('phone_number', models.CharField(max_length=13, validators=[apps.general.validators.phone_validate])),
                ('email', models.EmailField(max_length=254)),
                ('address_uz', models.CharField(max_length=40)),
                ('address_ru', models.CharField(blank=True, max_length=40)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('desc_uz', models.TextField(max_length=1400)),
                ('desc_ru', models.TextField(blank=True, max_length=1400)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('slug', models.SlugField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=20)),
                ('title_ru', models.CharField(max_length=20)),
                ('slug', models.SlugField(unique=True)),
                ('icon', models.ImageField(upload_to='services/icons/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='general/icon')),
                ('name', models.CharField(max_length=60)),
                ('slug', models.SlugField(unique=True)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=20)),
                ('title_uz', models.CharField(max_length=30)),
                ('title_ru', models.CharField(blank=True, max_length=30)),
                ('slug', models.SlugField(unique=True)),
                ('desc_uz', models.TextField(max_length=100)),
                ('desc_ru', models.TextField(blank=True, max_length=100)),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.subcategory')),
            ],
        ),
    ]
