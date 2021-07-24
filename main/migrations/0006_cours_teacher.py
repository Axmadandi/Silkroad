# Generated by Django 3.2 on 2021-07-21 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_yangiliklar_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Nomi')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='*')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('surname', models.CharField(max_length=50, verbose_name='Surname')),
                ('slug', models.SlugField(unique=True, verbose_name='*')),
                ('tajribasi', models.CharField(max_length=50, verbose_name='Ish Tajribasi')),
                ('natijasi', models.CharField(max_length=50, verbose_name='Natijasi')),
                ('body', models.TextField(verbose_name='Qisqacha Malumot')),
                ('cours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='main.cours')),
            ],
        ),
    ]