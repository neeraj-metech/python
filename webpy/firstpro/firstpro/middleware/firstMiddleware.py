from django.core.exceptions import PermissionDenied


class FilterIPMiddleware(object):
    def __init__(self, get_response):
        """
        One-time configuration and initialisation.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Code to be executed for each request before the view (and later
        middleware) are called.
        """
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        Called just before Django calls the view.
        """
        # user_id = view_kwargs.get('id', None)
        # if user_id:
        #     print(user_id)
        # if request.method == 'POST':
        #     print(request.POST.get('name'))
        path = request.path
        if path == '/contact':
            self.contactPath()
        # import pdb
        # pdb.set_trace()
        return None

    def process_exception(self, request, exception):
        """
        Called when a view raises an exception.
        """
        return None

    def process_template_response(self, request, response):
        """
        Called just after the view has finished executing.
        """
        return response

    # Check if client IP is allowed
    def process_request(self, request):
        allowed_ips = ['192.168.1.1', '123.123.123.123']  # Authorized ip's
        ip = request.META.get('REMOTE_ADDR')  # Get client IP
        # print(ip)
        if ip not in allowed_ips:
            raise PermissionDenied  # If user is not allowed raise Error
        # If IP is allowed we don't do anything
        return None

    def contactPath(self):
        print('it is coming for contact path only.')
