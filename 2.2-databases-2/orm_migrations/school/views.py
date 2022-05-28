from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


# class StudentsList(ListView):
#     model = Student
#     template_name = 'school/students_list.html'


def students_list(request):
    template = 'school/students_list.html'
    student_obj = Student.objects.order_by('group').prefetch_related('teachers')
    context = {'object_list': student_obj}
    return render(request, template, context)
