from django.contrib import admin
from .models import AnimalInfo, ZooCollection, ZooRecognization

admin.site.register(AnimalInfo)
admin.site.register(ZooCollection)
admin.site.register(ZooRecognization)
