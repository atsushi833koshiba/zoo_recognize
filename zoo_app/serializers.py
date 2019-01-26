from rest_framework import serializers
from .models import ZooRecognization

class ZooRecognizationSerializers(serializers.ModelSerializer):
    class Meta:
        model = ZooRecognization
        fields = ('name','score')
