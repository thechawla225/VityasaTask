# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import json
from rest_framework.decorators import api_view
from django.http import HttpResponseForbidden
from django.http import JsonResponse

points = []
temp2 = "Success "
@api_view(['POST'])
def plot(request):
    found = False
    output = {}
    point = []
    point_data = json.loads(request.body)
    x = point_data['x']
    y = point_data['y']
    point.append(x)
    point.append(y)
    points.append(point)
    if len(points) >= 4:
        checker, answer = check_square(found)
        if(checker):
            found = True
            output['status'] = answer
            return JsonResponse(output)
        else:
            output['status'] = 'accepted'
            return JsonResponse(output)
    else:
        output['status'] = 'accepted'
        return JsonResponse(output)
    

def check_square(found):
    temp = "Success "
    if(found):
        return True, temp2
    else:
        for i in points:
            for j in points:
                for k in points:
                    for l in points:
                        if(is_square(i,j,k,l)):
                            temp = temp + str(i) + " " + str(j) + " " + str(k) + " " + str(l)
                            temp2 = temp
                            return True, temp.replace('[', '(').replace(']', ')')
        return False, ""
def dist(p,q):
    return (p[0] - q[0])**2 + (p[1] - q[1])**2

def is_square(p1,p2,p3,p4):
    d2 = dist(p1, p2)
    d3 = dist(p1, p3)
    d4 = dist(p1, p4)
 
    if d2 == 0 or d3 == 0 or d4 == 0:   
        return False

    if d2 == d3 and 2 * d2 == d4 and \
                    2 * dist(p2, p4) == dist(p2, p3):
        return True
    if d3 == d4 and 2 * d3 == d2 and \
                    2 * dist(p3, p2) == dist(p3, p4):
        return True
 
    if d2 == d4 and 2 * d2 == d3 and \
                    2 * dist(p2, p3) == dist(p2, p4):
        return True
 
    return False
