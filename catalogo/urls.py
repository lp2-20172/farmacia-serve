
from django.conf.urls import url, include
from rest_framework import routers
from .views.categoria_view import CategoriaViewSet
from .views.producto_view import ProductoViewSet
from .views.compra_view import CompraViewSet


router = routers.DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'compras', CompraViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
