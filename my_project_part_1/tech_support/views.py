# Задание 1. tech support.py

from django.http import JsonResponse
from tech_support.models import Statistic


def statistics(request):
    stat_list = Statistic.objects.all()
    response = []
    for stat in stat_list:
        response.append(
            {
                "id": stat.id,
                "store": stat.store,
                "author": stat.author,
                "status": stat.status,
                "day": stat.day,
                "reason": stat.reason,
                "timestamp": stat.timestamp
            }
        )
    return JsonResponse(response, safe=False)
