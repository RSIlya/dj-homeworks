from rest_framework import serializers

from measurement.models import Sensor, Measurement

class SensorsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = (
            'temperature',
            'created_at',
        )


class SensorSerializer(serializers.ModelSerializer):
    values = MeasurementSerializer(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = ('id', 'name', 'description', 'values')


class AddMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'
