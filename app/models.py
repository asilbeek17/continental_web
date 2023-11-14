from django.db import models


class PlanningCourses(models.Model):
    class TypeChoice(models.TextChoices):
        toq = 'toq'
        juft = 'juft'

    image = models.ImageField(upload_to="new_coourses/", verbose_name="Kursning rasmi")
    title = models.CharField(max_length=155, verbose_name="Kursning nomi")
    description = models.TextField(verbose_name="Kurs haqida qisqacha")
    opening_date = models.DateField(verbose_name="Ochiladigan sana")
    day_type = models.CharField(max_length=10, choices=TypeChoice.choices, default=TypeChoice.toq)
    beginning_time = models.TimeField(verbose_name="Boshlanish vaqti")
    ending_time = models.TimeField(verbose_name="Tugash vaqti")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Yaqinda ochiladigan kurslar"
        verbose_name_plural = "Yaqinda ochiladigan kurslar"


class Courses(models.Model):
    class TypeChoice(models.TextChoices):
        toq = 'toq'
        juft = 'juft'

    image = models.ImageField(upload_to="Kursing rasmi/")
    beginning_time = models.TimeField(verbose_name="Boshlanish vaqti")
    day_type = models.CharField(max_length=10, choices=TypeChoice.choices, default=TypeChoice.toq)
    ending_time = models.TimeField(verbose_name="Tugash vaqti")
    title = models.CharField(max_length=155, verbose_name="Kursning nomi")
    description = models.TextField(verbose_name="Kurs haqida qisqacha")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Mavjud kurslar"
        verbose_name_plural = "Mavjud kurslar"


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name="Yangilikning nomi")
    description = models.TextField(verbose_name="Yangilik haqida")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Yangiliklar"
        verbose_name_plural = "Yangiliklar"


class Contact(models.Model):
    full_name = models.CharField(max_length=155)
    phone_number = models.CharField(max_length=13)
    level = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Xabarlar"
        verbose_name_plural = "Xabarlar"
