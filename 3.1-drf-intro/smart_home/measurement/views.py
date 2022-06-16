# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework import generics
from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorsListSerializer, AddMeasurementSerializer


class SensorListCreate(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsListSerializer


class SensorDetailUpdate(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorMeasurement(generics.ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = AddMeasurementSerializer

