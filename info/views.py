from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse


class InfoView(TemplateView):
    template_name = 'info.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})
