from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from mongo_auth.permissions import AuthenticatedOnly

from .models import Presentation
from .serializers import PresentationSerializer

class PresentationView(APIView):

    permission_classes = [AuthenticatedOnly]
    def get(self, request):
	    serializer = PresentationSerializer(Presentation.objects.all(), many=True)
	    response = {"presentations": serializer.data}
	    return Response(response, status=status.HTTP_200_OK)



    def post(self, request, format=None):

    	data = request.data
    	serializer = PresentationSerializer(data=data)
    	if serializer.is_valid():
    		presentation = Presentation(**data)
    		presentation.save()
    		response = serializer.data
    		return Response(response, status=status.HTTP_200_OK)
