from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework import status

from inscriptions.models import Boat , Rower , Leader , Category
from inscriptions.serializers import BoatSerializer , RowerSerializer , LeaderSerializer , CategorySerialier
# Create your views here.

class BoatViewSet (viewsets.ModelViewSet):
	queryset = Boat.objects.all()
	serializer_class = BoatSerializer

	@detail_route(methods=['post'])
	def pay(self, request, pk=None):

		try:
			boat = Boat.objects.get(id=pk)
		except Snippet.DoesNotExist:
			return HttpResponse(status=404)

		boat.payment = True
		boat.save()
		return Response({'status': 'payment set'})

	@detail_route(methods=['post'])
	def valid(self, request, pk=None):

		try:
			boat = Boat.objects.get(id=pk)
		except Snippet.DoesNotExist:
			return HttpResponse(status=404)

		boat.valid = True
		boat.save()
		return Response({'status': 'validation set'})



class RowerViewSet (viewsets.ModelViewSet):
	queryset = Rower.objects.all()
	serializer_class = RowerSerializer

class LeaderViewSet (viewsets.ModelViewSet):
	queryset = Leader.objects.all()
	serializer_class = LeaderSerializer

class CategoryViewSet (viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerialier