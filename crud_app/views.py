from django.shortcuts import render
from .models import Student
from django.contrib import messages
from django.db.models import Q

# Create your views here.


def index(request):
    students = Student.objects.all()
    query = ""
    if request.method == "POST":
        if "add" in request.POST:
            name = request.POST.get("name")
            email = request.POST.get("email")
            Student.objects.create(name=name, email=email)
            messages.success(request, "Student added succesfully")
        elif "update" in request.POST:
            id = request.POST.get("id")
            name = request.POST.get("name")
            email = request.POST.get("email")
            student = Student.objects.get(id=id)
            student.name = name
            student.email = email
            student.save()
            messages.success(request, "Student update succesfully")
        elif "delete" in request.POST:
            id = request.POST.get("id")
            Student.objects.get(id=id).delete()
            messages.success(request, "Student delete succesfully")
        elif "search" in request.POST:
            query = request.POST.get("searchquery")
            print("➡ crud_app/views.py:33 query:", query)
            students = Student.objects.filter(
                Q(name__icontains=query) | Q(email__icontains=query)
            )
            # print("➡ crud_app/views.py:37 student:", student)

    context = {"students": students, "query": query}
    return render(request, "index.html", context=context)
