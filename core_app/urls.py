from django.urls import path
from core_app.views import *

urlpatterns = [
				path('test-api', TestAPI.as_view()),
				path('download-file/<int:id>/', DownloadFile.as_view())
			]