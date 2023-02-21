from django.urls import path
from django.views.decorators.cache import cache_page
from course.views import *

urlpatterns = [
    path('', CourseHome.as_view(), name='home'),
    path('details/<slug:course_slug>/', CourseDetails.as_view(), name='details'),

    path('class/<int:group_number>/subject/<slug:subject_slug>/',
         CourseByCategories.as_view(), name='by_categories'),

    path('add_book/', CourseAddBook.as_view(), name='add_book'),
]
