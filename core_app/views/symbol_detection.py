from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from django.conf import settings
from core_engine.utility import api_error_handler
from rest_framework.parsers import MultiPartParser
from core_app.models import DetectedFile
from core_app.serializers import ImageSerializer
from django.shortcuts import get_object_or_404



class TestAPI(APIView):
	def get(self, request, *args, **kargs):
		try:
			# data = get_object_or_404(DetectedFile, id=38)
			# print("data", data)
			return JsonResponse({'data': [], 'error': False, 'message': 'Test API running successfully123'})
		except Exception as e:
			error = api_error_handler.PrintException()
			return JsonResponse({'data':error, 'error': True, 'message': 'Something went wrong'}, status=500)

