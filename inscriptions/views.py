from django.shortcuts import render
from rest_framework import viewsets
from inscriptions.models import Boat , Rower , Leader , Category
from inscriptions.serializers import BoatSerializer , RowerSerializer , LeaderSerializer , CategorySerialier
# Create your views here.

class BoatViewSet (viewsets.ModelViewSet):
	queryset = Boat.objects.all()
	serializer_class = BoatSerializer

class RowerViewSet (viewsets.ModelViewSet):
	queryset = Rower.objects.all()
	serializer_class = RowerSerializer

class LeaderViewSet (viewsets.ModelViewSet):
	queryset = Leader.objects.all()
	serializer_class = LeaderSerializer

class CategoryViewSet (viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerialier