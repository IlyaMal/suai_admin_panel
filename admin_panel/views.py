from django.shortcuts import render, redirect
from django.views import View
from django.http.request import HttpRequest
from django.urls import reverse
from functools import wraps


# Create your views here.
def is_admin(view_func):
    @wraps(view_func)
    def _wrapped_view(self, request: HttpRequest, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_staff:
            return redirect(reverse("admin_panel:index"))
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
        request_files = request.FILES
        print(request_data, request_files)
        return redirect(reverse("admin_panel:index"))