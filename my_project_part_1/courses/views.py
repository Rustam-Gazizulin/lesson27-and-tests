from courses.models import Course
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


def courses(request):
    courses_list = Course.objects.all()

    search_text = request.GET.get("author", None)
    if search_text:
        courses_list = courses_list.filter(author=search_text)
    response = []
    for course in courses_list:
        response.append(
            {
                "id": course.id,
                "slug": course.slug,
                "author": course.author,
                "description": course.description,
                "start_day": course.start_day,
                "status": course.status,
                "created": course.created,
            }
        )
    return JsonResponse(response, safe=False)


def new_courses(request):
    cours_new = Course.objects.filter(status="new")
    response = []
    for course in cours_new:
        response.append(
            {
                "id": course.id,
                "slug": course.slug,
                "author": course.author,
                "description": course.description,
                "start_day": course.start_day,
                "status": course.status,
                "created": course.created,
            }
        )
    return JsonResponse(response, safe=False)


def get_course(request, slug):
    course = Course.objects.get(slug=slug)
    return JsonResponse(
        {
            "id": course.id,
            "slug": course.slug,
            "author": course.author,
            "description": course.description,
            "start_day": course.start_day,
            "status": course.status,
            "created": course.created,
        }
    )


def search(request):
    courses_search = Course.objects.all()

    search_text = request.GET.get("author", None)
    if search_text:
        courses_search = courses_search.filter(author=search_text)
#
    response = []
    for course in courses_search:
        response.append(
            {
                "id": course.id,
                "slug": course.slug,
                "author": course.author,
                "description": course.description,
                "start_day": course.start_day,
                "status": course.status,
                "created": course.created,
            }
        )
    return JsonResponse(response, safe=False)
