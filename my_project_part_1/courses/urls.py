from django.urls import path
from courses import views



# TODO настройте здесь urls для заданий сourses, new_courses, find_by_name, who's_author
urlpatterns = [
    path("", views.courses, name="courses"),
    path("new/", views.new_courses, name="new_courses"),
    path("<str:slug>/", views.get_course, name="get_course"),
]
