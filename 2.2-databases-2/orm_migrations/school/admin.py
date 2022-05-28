from django.contrib import admin

from .models import Student, Teacher


class RelationsInline(admin.StackedInline):
    model = Student.teachers.through
    extra = 1

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'group')
    inlines = [
        RelationsInline,
    ]
    exclude = ('teachers',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')
    inlines = [
        RelationsInline,
    ]

