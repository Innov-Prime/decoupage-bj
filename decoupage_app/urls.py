from django.urls import path
from rest_framework.routers import DefaultRouter
from decoupage_app import views


urlpatterns = [
    path('departements/', views.departementView, name='departemants'),
    path('<id_dep>/communes/', views.communeView, name='communes'),
    path('<id_com>/arrondissements/', views.arrondissementView, name='arrondissements'),
    path('<id_arrond>/quatiers/', views.quartierView, name='quartier')
]