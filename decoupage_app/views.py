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

def communeView(request):
    id_dep = request.GET.get('id_dep')
    queryset = Commune.objects.filter(id_dep=id_dep).order_by('lib_com')

    serialization = CommuneSerializer(queryset, many=True)
    return Response(serialization.data)

def arrondissementView(request):
    id_com = request.GET.get('id_com')
    queryset = Arrondissement.objects.filter(id_com=id_com).order_by('lib_arrond')

    serialization = ArrondissementSerializer(queryset, many=True)
    return Response(serialization.data)

def quartierView(request):
    id_arrond = request.GET.get('id_arrond')
    queryset = Arrondissement.objects.filter(id_arrond=id_arrond).order_by('lib_quart')

    serialization = ArrondissementSerializer(queryset, many=True)
    return Response(serialization.data)

"""
@api_view(['GET'])
class DepartementViewSet(viewsets.ModelViewSet):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer


@api_view
class CommuneViewSet(viewsets.ModelViewSet):
    queryset = Commune.objects.all()
    serializer_class = CommuneSerializer
    
    # def get_queryset(self):
    #     queryset = Commune.objects.all()
    #     id_depart = self.request.query_params.get('id_depart')
    #     if id_depart is not None :
    #         queryset = queryset.filter(id_depart=id_depart).order_by('lib_com')
    #     return queryset

@api_view
class ArrondissementViewSet(viewsets.ModelViewSet):
    queryset = Arrondissement.objects.all()
    serializer_class = ArrondissementSerializer

@api_view
class QuartierViewSet(viewsets.ModelViewSet):
    queryset = Quartier.objects.all()
    serializer_class = QuartierSerializer
"""