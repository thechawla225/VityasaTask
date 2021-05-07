# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import json
from rest_framework.decorators import api_view
from django.http import HttpResponseForbidden
from django.http import JsonResponse

slots = {}
bookings = []


@api_view(['POST', 'GET'])
def booking(request):
    if request.method == 'POST':
        output = {'status': 'confirmed'}
        book_data = json.loads(request.body)
        if book_data['slot'] <= 23 and book_data['slot'] >= 0:
            if book_data['slot'] in slots and slots[book_data['slot']] \
                < 2:
                slots[book_data['slot']] += 1
                for i in bookings:
                    if i['slot'] == book_data['slot']:
                        temp = i['name']
                        name = []
                        name.append(temp)
                        name.append(book_data['name'])
                        i['name'] = name
            elif book_data['slot'] not in slots:
                slots[book_data['slot']] = 1
                bookings.append(book_data)
            else:
                status = 'slot full, unable to save booking for ' \
                    + book_data['name'] + ' in slot ' \
                    + str(book_data['slot'])
                output['status'] = status
            return JsonResponse(output)
    elif request.method == 'GET':
        return JsonResponse(bookings, safe=False)


@api_view(['POST'])
def cancel(request):
    output = {}
    cancel_data = json.loads(request.body)
    for booking in bookings:
        if booking['slot'] == cancel_data['slot']:
            status = 'canceled booking for ' + cancel_data['name'] \
                + ' in slot ' + str(cancel_data['slot'])
            try:
                booking['name'].remove(cancel_data['name'])
                temp = booking['name'][0]
                booking['name'] = temp
            except:
                bookings.remove(booking)

            output['status'] = status
            return JsonResponse(output)

    status = 'no booking for ' + cancel_data['name'] + ' in slot ' \
        + str(cancel_data['slot'])
    output['status'] = status
    return JsonResponse(output)
