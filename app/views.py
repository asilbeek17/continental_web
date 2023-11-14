from django.shortcuts import render
from app.models import PlanningCourses, Courses, News, Contact


def index(request):
    plan_course = PlanningCourses.objects.all()
    course = Courses.objects.all()

    context = {
        'plan_courses': plan_course,
        'courses': course
    }

    return render(request, 'main/index.html', context)


def courses(reques):
    course = Courses.objects.all()

    context = {
        'courses': course
    }

    return render(reques, 'main/courses.html', context)


def news(request):
    new = News.objects.all()

    context = {
        "news": new
    }

    return render(request, 'main/news.html', context)


def gallery(request):
    return render(request, 'main/gallery.html')


def contact(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        level = request.POST.get('level')
        text = request.POST.get('text')

        c = Contact(full_name=full_name, phone_number=phone_number, level=level, text=text)
        c.save()

    return render(request, 'main/contact.html')
