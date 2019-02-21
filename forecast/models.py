# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_email = models.EmailField(max_length=100, default='')


class wheather(models.Model):
    created_datetime = models.DateTimeField('created date of record')
    weather_date = models.CharField(max_length=10, primary_key=True)
    min_temp = models.IntegerField(default=0)
    max_temp = models.IntegerField(default=0)
    wind = models.IntegerField(default=0)
    rain = models.CharField(max_length=10)


def save_weather_record(data):
    record = wheather(created_datetime=timezone.now(), weather_date=data['weather_Date'], min_temp=data['min_temp'],
                      wind=data['wind'], max_temp=data['max_temp'], rain=data['rain'])
    record.save()


def get_weather_records(offset=None):
    results = wheather.objects.order_by('created_datetime').all()[:10]
    data = [[item.weather_date, item.min_temp, item.max_temp, item.wind, item.rain] for item in results]
    return data

