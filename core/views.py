from .models import User
from .models import Person
from rest_framework import serializers, viewsets


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        #fields = '__all__'
        fields = ('id', 'username', 'email', 'is_staff')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        #fields = '__all__'
        fields = ('id', 'username', 'email', 'is_staff')


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
