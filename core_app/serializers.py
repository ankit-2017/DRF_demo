from rest_framework import serializers
from core_app.models import DetectedFile

class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = DetectedFile
		fields = ('id', 'file', 'count', 'created_at')