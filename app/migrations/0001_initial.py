# Generated by Django 4.2.7 on 2023-11-12 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Kursing rasmi/')),
                ('beginning_time', models.TimeField(verbose_name='Boshlanish vaqti')),
                ('ending_time', models.TimeField(verbose_name='Tugash vaqti')),
                ('title', models.CharField(max_length=155, verbose_name='Kursning nomi')),
                ('description', models.TextField(verbose_name='Kurs haqida qisqacha')),
            ],
            options={
                'verbose_name': 'Mavjud kurslar',
                'verbose_name_plural': 'Mavjud kurslar',
            },
        ),
        migrations.CreateModel(
            name='PlanningCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='new_coourses/', verbose_name='Kursning rasmi')),
                ('title', models.CharField(max_length=155, verbose_name='Kursning nomi')),
                ('description', models.TextField(verbose_name='Kurs haqida qisqacha')),
                ('opening_date', models.DateField(verbose_name='Ochiladigan sana')),
                ('day_type', models.CharField(choices=[('toq', 'Toq'), ('juft', 'Juft')], default='toq', max_length=10)),
                ('beginning_time', models.TimeField(verbose_name='Boshlanish vaqti')),
                ('ending_time', models.TimeField(verbose_name='Tugash vaqti')),
            ],
            options={
                'verbose_name': 'Yaqinda ochiladigan kurslar',
                'verbose_name_plural': 'Yaqinda ochiladigan kurslar',
            },
        ),
    ]
