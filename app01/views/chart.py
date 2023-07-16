from django.shortcuts import render
from django.http import JsonResponse


def chart_list(request):
    return render(request, 'char_list.html')


def chart_col(request):
    series = [
        {
            "name": 'Tokyo',
            "data": [49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]
        },
        {
            "name": 'test',
            "data": [49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]
        }
    ]
    categories = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

    result = {
        "status" : True,
        "data" : {
            "series" : series,
            "categories":categories,
        }
    }

    return JsonResponse(result)
