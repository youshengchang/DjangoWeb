from django.http import HttpResponse

class MiddlewareLifeCycle:
    def __init__(self, get_response):
        print("INIT MIDDLEWARE")
        self.get_response = get_response

    def __call__(self, request):
        print("Before the view is executed")
        response = self.get_response(request)
        print("After the view is executed")
        return response

class ExceptionHandlingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        print(exception.__class__.__name__)
        print(exception)
        return HttpResponse("<b>WE currently has issue. Please return back in couple min.</b>")
