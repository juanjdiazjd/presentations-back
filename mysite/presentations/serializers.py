
from rest_framework_mongoengine import serializers

from .models import Presentation

class PresentationSerializer(serializers.DocumentSerializer):
    class Meta:
    	model = Presentation
    	fields = '__all__'