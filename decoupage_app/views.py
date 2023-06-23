from django.shortcuts import render
from rest_framework import viewsets

from decoupage_app.models import Departement, Quartier, Arrondissement, Commune
from decoupage_app.serializers import DepartementSerializer, CommuneSerializer, ArrondissementSerializer, QuartierSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def departementView(request):
    queryset = Departement.objects.all()
    serialization = DepartementSerializer(queryset, many=True)
    return Response(serialization.data)

@api_view(['GET'])
def arrondissementsView(request):
    queryset = Arrondissement.objects.all()
    serialization = ArrondissementSerializer(queryset, many=True)
    return Response(serialization.data)

@api_view(['GET'])
def communesView(request):
    queryset = Commune.objects.all()
    serialization = CommuneSerializer(queryset, many=True)
    return Response(serialization.data)

@api_view(['GET'])
def quartiersView(request):
    queryset = Quartier.objects.all()
    serialization = QuartierSerializer(queryset, many=True)
    return Response(serialization.data)

@api_view(['GET'])
def communeView(request, id_dep):
    queryset = Commune.objects.filter(id_dep=id_dep).order_by('lib_com')
    serialization = CommuneSerializer(queryset, many=True)
    return Response(serialization.data)

@api_view(['GET'])
def arrondissementView(request, id_com):
    queryset = Arrondissement.objects.filter(id_com=id_com).order_by('lib_arrond')
    serialization = ArrondissementSerializer(queryset, many=True)
    return Response(serialization.data)

@api_view(['GET'])
def quartierView(request, id_arrond):
    queryset = Quartier.objects.filter(id_arrond=id_arrond).order_by('lib_quart')
    serialization = QuartierSerializer(queryset, many=True)
    return Response(serialization.data)