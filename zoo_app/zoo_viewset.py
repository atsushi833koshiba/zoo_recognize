from rest_framework import viewsets, routers
from rest_framework.response import Response
from rest_framework.decorators import list_route
from .serializers import ZooRecognizationSerializers
from .models import ZooRecognization


class ZooViewSet(viewsets.ModelViewSet):
    queryset = ZooRecognization.objects.all()
    serializer_class = ZooRecognizationSerializers


router = routers.DefaultRouter()
router.register(r'recognize', ZooViewSet)
