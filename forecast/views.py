# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from forecast.models import wheather
from forecast.serializers import wheatherSerializer
from forecast.forms import ExtendedUserCreationForm


def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../profile')
        else:
            error = str(form.errors)
            form = ExtendedUserCreationForm()
            args = {'form': form, 'error': error}
            return render(request, 'forecast/reg_form.html', args)
    else:
        form = ExtendedUserCreationForm()
        args = {'form': form, 'error': ''}
        return render(request, 'forecast/reg_form.html', args)


def profile(request):
    args = {'user': request.user}
    return render(request, 'forecast/profile.html', args)


@csrf_exempt
def get_graph_data(request):
    from django.http import JsonResponse
    from forecast.models import get_weather_records

    data = get_weather_records(offset=None)

    data = {
        'json_data': data
    }
    return JsonResponse(data)


@csrf_exempt
def weather_list(request):
    """
        List all weather records.
    """
    # TODO, Validate that only logged in users get to
    if request.method == 'GET':
        weather_obj = wheather.objects.all()
        serializer = wheatherSerializer(weather_obj, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse('no other requests allowed', status=400)
