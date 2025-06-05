from django.contrib.auth.decorators import user_passes_test

def role_required(role):
    def decorator(view_func):
        decorated_view_func = user_passes_test(
            lambda user: user.is_authenticated and user.role == role
        )(view_func)
        return decorated_view_func
    return decorator