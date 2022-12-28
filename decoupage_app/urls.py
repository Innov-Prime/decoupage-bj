from django.urls import path
from rest_framework.routers import DefaultRouter
from decoupage_app import views

# from decoupage_app.views import DepartementViewSet, CommuneViewSet, ArrondissementViewSet, QuartierViewSet

urlpatterns = [
    path('departements/', views.departementView, name = 'departemants'),
    path('communes/', views.communeView, name = 'communes'),
    path('arrondissements/', views.arrondissementView, name = 'arrondissements'),
    path('quatiers/', views.quartierView, name = 'quartier')
]