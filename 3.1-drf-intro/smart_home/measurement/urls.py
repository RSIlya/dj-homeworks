from django.urls import path

from measurement.views import SensorListCreate, SensorDetailUpdate, SensorMeasurement

urlpatterns = [
    path('sensors/', SensorListCreate.as_view()),
    path('sensors/<pk>/', SensorDetailUpdate.as_view()),
    path('measurements/', SensorMeasurement.as_view()),
]
