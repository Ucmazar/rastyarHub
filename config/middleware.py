# myproject/middleware.py

from django.utils import translation

class AdminLocaleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # اگر مسیر ادمین است زبان انگلیسی شود
        if request.path.startswith('/admin/'):
            translation.activate('en')
            request.LANGUAGE_CODE = 'en'
        else:
            # بقیه مسیرها زبان پیش‌فرض پروژه است
            translation.activate('fa')
            request.LANGUAGE_CODE = 'fa'

        response = self.get_response(request)
        translation.deactivate()
        return response
