from django.urls import path
from .views import students_page_view, main_page_view

urlpatterns = [
    path('main/', main_page_view, name='main_page'),
    path('students/', students_page_view, name='students_page'),
]
