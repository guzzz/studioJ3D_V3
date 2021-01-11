
from rest_framework import serializers

from .models import Project


class ProjectCustomSerializer(serializers.ModelSerializer):
	photo_url = serializers.ReadOnlyField(source='photo.url')
	small_photo_url = serializers.ReadOnlyField(source='small_photo.url')

	class Meta:
		model = Project
		fields = '__all__'
