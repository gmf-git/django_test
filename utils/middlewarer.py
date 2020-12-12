from django.http import JsonResponse, HttpResponse
from django.utils.deprecation import MiddlewareMixin


class AuthMIDDLEWARE(MiddlewareMixin):

    def process_response(self, request, response):
        method = request.method
        status = response.status_code
        if request.path == "/docs/":
            return response
        if method != 'get' and '2' in str(status):
            response.data = {
                'status': 200,
                'msg': '请求成功'
            }
            response._is_rendered = False
            response.render()
        print(response.data)
        return response
