# Generated by Django 3.2 on 2021-07-15 12:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_author_category_yangiliklar'),
    ]

    operations = [
        migrations.AddField(
            model_name='yangiliklar',
            name='body',
            field=models.TextField(default=datetime.datetime(2021, 7, 15, 12, 10, 15, 815724, tzinfo=utc), max_length=1000, verbose_name='Text'),
            preserve_default=False,
        ),
    ]