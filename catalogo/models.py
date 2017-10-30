from django.db import models
from core.models import User, Person

# Create your models here.


class Categoria(models.Model):

    nombre = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return '%s' % (self.nombre)


class UnidadMed(models.Model):

    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        verbose_name = "UnidadMed"
        verbose_name_plural = "UnidadMeds"

    def __str__(self):
        return '%s (%s)' % (self.codigo, self.nombre)


class Almacen(models.Model):

    nombre = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Almacen"
        verbose_name_plural = "Almacenes"

    def __str__(self):
        return '%s (%s)' % (self.nombre, self.direccion,)


class Producto(models.Model):

    nombre = models.CharField(max_length=60)
    codigo = models.CharField(max_length=10, null=True, blank=True)
    detalle = models.TextField(null=True, blank=True)
    fechaVen = models.DateField(auto_now_add=False)
    precio_venta = models.FloatField(default=0.0)
    unidad_med = models.ForeignKey(UnidadMed)
    almacen = models.ForeignKey(Almacen)
    categoria = models.ManyToManyField(
        "Categoria",
        verbose_name="list of Categorias",
        null=True,  blank=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return '%s (%s)' % (self.nombre, self.codigo)


class Cliente(models.Model):

    ruc = models.CharField(max_length=11)
    person = models.OneToOneField(Person)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return '%s' % (self.ruc)


class Venta(models.Model):

    nro_doc = models.CharField(max_length=15)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.FloatField(default=0)
    vendedor = models.ForeignKey(User)
    cliente = models.ForeignKey(Cliente, blank=True, null=True)
    almacen = models.ForeignKey(Almacen)

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    def __str__(self):
        return '%s' % (self.nro_doc)


class ShoppingCart(models.Model):

    cantidad = models.IntegerField(max_length=15)
    precio_uni = models.FloatField(default=0)

    producto = models.ForeignKey(Producto)
    venta = models.ForeignKey(Venta)

    class Meta:
        verbose_name = "ShoppingCart"
        verbose_name_plural = "ShoppingCarts"

    def __str__(self):
        return 'VENTA%s - PROD: %s' % (self.venta.nro_doc, self.producto.nombre,)


class Area (models.Model):

    nombre = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Area"

    def __str__(self):
        return '%s' % (self.nombre)


class DetalleCompra(models.Model):

    nro_doc = models.CharField(max_length=16)
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.FloatField(default=0)
    precio_unitario = models.FloatField(default=0.0)

    class Meta:
        verbose_name = "DetalleCompra"
        verbose_name_plural = "DetalleCompras"

    def __str__(self):
        return '%s' % (self.nro_doc)


class Proveedor(models.Model):

    empresa = models.CharField(max_length=10)
    ruc = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return '%s (%s)' % (self.empresa, self.ruc)


class Compra(models.Model):

    nro_doc = models.CharField(max_length=16)
    fecha = models.DateTimeField(auto_now_add=True)
    precio_total = models.FloatField(default=0.0)
    proveedor = models.OneToOneField(Proveedor)
    almacen = models.ForeignKey(Almacen)
    comprador = models.ForeignKey(User)

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"

    def __str__(self):
        return '%s' % (self.nro_doc)
