from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated
from core.models import Categoria
from core.serializers import CategoriaSerializers


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializers
    # permission_classes = [IsAuthenticated]
