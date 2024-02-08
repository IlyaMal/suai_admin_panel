from django.shortcuts import render, redirect
from django.views import View
from django.http.request import HttpRequest
from django.urls import reverse
from functools import wraps
from django.core.exceptions import PermissionDenied
from .services.mailer import send

def is_admin(view_func):
    @wraps(view_func)
    def _wrapped_view(self, request: HttpRequest, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            return redirect(reverse("admin:login"))
        return view_func(self, request, *args, **kwargs)
    return _wrapped_view


class IndexView(View):
    @is_admin
    def get(self, request):
        context = {"status": 200}
        return render(
                        request=request,
                        template_name='admin_panel/index.html',
                        context=context
                    )
    
    @is_admin
    def post(self, request):
        request_data = request.POST
        request_file = request.FILES.get("file")
        url = '/for/all'
        ids = None

        is_send_all = True if request_data.get("is_send_all") else False

        if not is_send_all:
            ids = [int(idx) for idx in request_data.get('ids').split(' ')]
            url = '/for/any'

        # send(f"http://0.0.0.0:8765{url}", request_data, request_file, ids)
        return redirect(reverse("admin_panel:index"))