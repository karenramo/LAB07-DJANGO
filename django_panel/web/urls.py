from django.urls import path

from . import views

app_name = 'web'

urlpatterns = [
    path('', views.AlumnoView.as_view(),name='index'),
    path('eliminar/<int:alumno_id>/', views.eliminar_alumno, name='eliminar'),
    path('profesor/', views.ProfesorView.as_view(), name='profesor'),
    path('eliminar_profesor/<int:profesor_id>/', views.eliminar_profesor, name='eliminar_profesor'),
]   