from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def teacher_view(request):
    # teacher_table = teachers.objects.all()
    teacher_table = "Hello"
    return HttpResponse(teacher_table)

def student_view(request):
    # students_table = students.objects.all()
    students_table = "Hi"
    return HttpResponse(students_table)


