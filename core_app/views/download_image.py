from rest_framework.views import Response
from wsgiref.util import FileWrapper
from django.http import HttpResponse
from rest_framework.views import APIView
from core_app.models import DetectedFile
from django.shortcuts import get_object_or_404
from core_engine.utility import api_error_handler
from core_app.serializers import ImageSerializer


class DownloadFile(APIView):
	def get(self, request, id, *args):
		try:
			query = get_object_or_404(DetectedFile, id=id)
			file_path = query.file.path
			document = open(file_path, 'rb')
			response = HttpResponse(FileWrapper(document), content_type='image/png')
			response['Content-Disposition'] = 'attachment; filename="%s"' % query.file.name
			# print("file path", file.path)
			return response
		except Exception as e:
			error = api_error_handler.PrintException()
			return Response({'data':error, 'error': True, 'message': 'Something went wrong'}, status=500)