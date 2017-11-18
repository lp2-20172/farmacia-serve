from ..models.unidadMed import UnidadMed
from rest_framework import serializers, viewsets
from rest_framework import permissions
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce


class UnidadMedSerializer(serializers.ModelSerializer):

    class Meta:
        model = UnidadMed
        fields = '__all__'
        #fields = ('id', 'username', 'email', 'is_staff')


class UnidadMedViewSet(viewsets.ModelViewSet):
    queryset = UnidadMed.objects.all()
    serializer_class = UnidadMedSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        queryall = (Q(codigo__icontains=query),
                    )
        queryset = self.queryset.filter(reduce(OR, queryall))
        return queryset
