from django.urls import path

# from school.views import StudentsList
#
# urlpatterns = [
#     path('', StudentsList.as_view()),
# ]


from school.views import students_list

urlpatterns = [
    path('', students_list, name='students'),
]