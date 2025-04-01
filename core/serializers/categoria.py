from rest_framework.serializers import ModelSerializer

from core.models import Categoria


class CategoriaSerializers(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"
