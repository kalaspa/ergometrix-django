from rest_framework import serializers
from inscriptions.models import Boat , Rower , Leader , Category

class BoatSerializer(serializers.ModelSerializer):
	class Meta:
		model = Boat

class RowerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rower

class LeaderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Leader

class CategorySerialier(serializers.ModelSerializer):
	class Meta:
		model = Category