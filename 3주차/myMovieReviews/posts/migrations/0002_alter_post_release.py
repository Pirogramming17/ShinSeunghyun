# Generated by Django 3.2.14 on 2022-07-15 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='release',
            field=models.IntegerField(verbose_name='개봉 연도'),
        ),
    ]
