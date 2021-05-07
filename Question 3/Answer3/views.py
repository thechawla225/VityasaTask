# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import json
from rest_framework.decorators import api_view
from django.http import HttpResponseForbidden
from django.http import JsonResponse

points = []


@api_view(['POST'])
def plot(request):
    output = {}
    point = []
    point_data = json.loads(request.body)
    x = point_data['x']
    y = point_data['y']
    point.append(x)
    point.append(y)
    points.append(point)
    if len(points) >= 4:
        for point1 in points:
            flag = 0
            check = []
            temp = 'Success ' + str(point1) + ' '
            till_now = []
            check.append(point1[0])
            check.append(point1[1])
            till_now.append(point1)
            for point2 in points:
                if point1 != point2:
                    if point2[0] in check and point2[1] in check:
                        temp = temp + str(point2) + ' '
                        till_now.append(point2)
                if len(till_now) == 4:
                    output['status'] = temp.replace('[', '('
                            ).replace(']', ')')
                    return JsonResponse(output)
        output['status'] = 'accepted'
        return JsonResponse(output)
    else:
        output['status'] = 'accepted'
        return JsonResponse(output)
