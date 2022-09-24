from cars.models import Car
from django.http import JsonResponse


def get_car(request, pk):
    car = Car.objects.get(pk=pk)
    return JsonResponse({
        "id": car.pk,
        "slug": car.slug,
        "name": car.name,
        "brand": car.brand,
        "address": car.address,
        "description": car.description,
        "status": car.status,
        "created": car.created
    })


def search(request):
    cars_list = Car.objects.all()

    search_brand = request.GET.get("brand", None)
    if search_brand:
        cars_list = cars_list.filter(brand=search_brand)

    response = []
    for car in cars_list:
        response.append(
            {
                "id": car.pk,
                "name": car.name,
                "brand": car.brand,
                "status": car.status,
            }
        )
    return JsonResponse(response, safe=False)
