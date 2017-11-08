from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Person(models.Model):

    nombre = models.CharField(max_length=60, blank=True, null=True)
    apellido = models.CharField(max_length=60, blank=True, null=True)
    email = models.EmailField(max_length=60, blank=True, null=True)
    estado = models.CharField(max_length=10, blank=True, null=True)
    codigo = models.CharField(max_length=10)
    lugar = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido, )


class User(AbstractUser):

    detalle = models.TextField(blank=True, null=True)
    person = models.OneToOneField(Person, blank=True, null=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return '%s' % (self.username)
