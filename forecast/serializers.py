from rest_framework import serializers
from forecast.models import wheather


class wheatherSerializer(serializers.ModelSerializer):
    weather_date = serializers.CharField(max_length=10)
    min_temp = serializers.IntegerField(default=0)
    max_temp = serializers.IntegerField(default=0)
    wind = serializers.IntegerField(default=0)
    rain = serializers.CharField(max_length=10)

    class Meta:
        model = wheather
        fields = ('created_datetime', 'weather_date', 'min_temp', 'max_temp', 'wind', 'rain')
