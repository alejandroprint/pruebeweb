from rest_framework import serializers
from .models import producto

class productoSerializers(serializers.ModelSerializer):
    class Meta :
        model = producto
        fields = ['marca','modelo','precio']