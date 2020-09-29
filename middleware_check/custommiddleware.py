class FirstMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        print('----- process request M1 -----')
        return None

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('----- process view M1 -----')
        print('----- Middleware view name : %s   M1-----' % view_func.__name__)
        return None

    def process_response(self, request, response):
        print('----- process response M1 -----')
        return response

    def __call__(self, request):
        """Handle new-style middleware here."""
        response = self.process_request(request)
        if response is None:
            # If process_request returned None, we must call the next middleware or
            # the view. Note that here, we are sure that self.get_response is not
            # None because this method is executed only in new-style middlewares.
            response = self.get_response(request)

        response = self.process_response(request, response)
        return response


class SecondMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        print('----- process request M2 -----')
        return None

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('----- process view M2 -----')
        print('----- Middleware view name : %s   M2-----' % view_func.__name__)
        return None

    def process_response(self, request, response):
        print('----- process response M2 -----')
        return response

    def __call__(self, request):
        """Handle new-style middleware here."""
        response = self.process_request(request)
        if response is None:
            # If process_request returned None, we must call the next middleware or
            # the view. Note that here, we are sure that self.get_response is not
            # None because this method is executed only in new-style middlewares.
            response = self.get_response(request)

        response = self.process_response(request, response)
        return response