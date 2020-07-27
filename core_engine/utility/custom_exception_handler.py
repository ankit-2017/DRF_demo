from rest_framework.views       import exception_handler as drf_exception_handler
from django.http	            import JsonResponse

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = drf_exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status'] = response.status_code
        response.data['data']	=  []
    return response


#call this function to handle 404 error
def error404(request, exception):
	return JsonResponse({'data':[], 'error': True, 'message': 'Url not found'}, status=404)

#call this function to handle 500 error
def error500(exception):
	return JsonResponse({'data':[], 'error': True, 'message': 'Internal server error'}, status=500)




	