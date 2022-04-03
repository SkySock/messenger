from django.conf import settings


class CORSMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["Access-Control-Allow-Origin"] = settings.ORIGIN_ALLOWED_HOST
        response["Access-Control-Allow-Headers"] = 'content-type, Authorization'
        response['Access-Control-Allow-Credentials'] = 'true'
        response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, HEAD, OPTIONS, PATCH'

        return response
