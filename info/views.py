from django.shortcuts import render
from django.views.generic import TemplateView
from info.models import Questions
from django.http import JsonResponse


class InfoView(TemplateView):
    template_name = 'info.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})


class PythonView(TemplateView):
    template_name = 'python.html'

    def get(self, request, *args, **kwargs):
        context = {
            "questions": list(Questions.objects.filter(question_code="Py").values("statement", "answer"))
        }
        return render(request, self.template_name, context=context)


class DjangoView(TemplateView):
    template_name = 'django.html'

    def get(self, request, *args, **kwargs):
        context = {
            "questions": list(Questions.objects.filter(question_code="Dj").values("statement", "answer"))
        }
        return render(request, self.template_name, context=context)
