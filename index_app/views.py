from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(
            request,
            template_name="index_app/index.html",
            context={})
