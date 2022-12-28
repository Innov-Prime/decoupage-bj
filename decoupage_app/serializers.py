from rest_framework import serializers

from decoupage_app.models import Departement, Commune, Arrondissement, Quartier


class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = '__all__'


class CommuneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commune
        fields = '__all__'


class ArrondissementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Arrondissement
        fields = '__all__'


class QuartierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quartier
        fields = '__all__'