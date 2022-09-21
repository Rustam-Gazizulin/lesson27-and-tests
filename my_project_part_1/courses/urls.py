from django.urls import path
from courses.views import courses



# TODO настройте здесь urls для заданий сourses, new_courses, find_by_name, who's_author
urlpatterns = [
    path("courses/", courses),
]
