# Generated by Django 4.2.7 on 2023-11-12 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_courses_day_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Yangilikning nomi')),
                ('description', models.TextField(verbose_name='Yangilik haqida')),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Yangiliklar',
                'verbose_name_plural': 'Yangiliklar',
            },
        ),
    ]
