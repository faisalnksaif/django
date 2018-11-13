from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.registerStudent, name='registerStudent'),
    path('all-students', views.getAllStudents, name='getAllStudents'),
    path('delete-student', views.deleteStudent, name='deleteStudent'),
]