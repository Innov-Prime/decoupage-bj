from django.urls import path
from rest_framework.routers import DefaultRouter
from decoupage_app import views


urlpatterns = [
    path('departements/', views.departementView, name='departemants'),
    path('arrondissements/', views.arrondissementsView, name='arrondissements'),
    path('communes/', views.communesView, name='communes'),
    path('quartiers/', views.quartiersView, name='quartiers'),
    path('<id_dep>/communes/', views.communeView, name='communes'),
    path('<id_com>/arrondissements/', views.arrondissementView, name='arrondissements'),
    path('<id_arrond>/quartiers/', views.quartierView, name='quartiers')
]