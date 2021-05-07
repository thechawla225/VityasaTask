# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.decorators import api_view
from django.http import HttpResponseForbidden
from django.http import JsonResponse
from sys import maxsize


@api_view(['POST'])
def items(request):
    checkArray = request.GET.getlist('data')
    valid_entries = 0
    invalid_entries = 0
    sum = 0
    mini = maxsize
    maxi = 0
    output = {}
    for i in checkArray:
        if i.isnumeric() and int(i) > 0:
            valid_entries += 1
            maxi = max(maxi, int(i))
            mini = min(mini, int(i))
            sum = sum + int(i)
        else:
            invalid_entries += 1
    output['valid_entries'] = valid_entries
    output['invalid_entries'] = invalid_entries
    output['min'] = mini
    output['max'] = maxi
    output['average'] = sum / valid_entries

    return JsonResponse(output)
