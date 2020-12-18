from django.http import HttpResponseRedirect
from functools import wraps


def is_manager(test_func=None, login_url=None, redirect_field_name=None):
    def decorator(function):
        @wraps(function)
        def wrap(request, *args, **kwargs):
            if request.user.is_authenticated:
                if request.user.is_manager:
                    return function(request, *args, **kwargs)
                return HttpResponseRedirect(redirect_field_name)
            return HttpResponseRedirect(redirect_field_name)
        return wrap
    return decorator
