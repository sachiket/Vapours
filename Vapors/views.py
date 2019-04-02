from django.views.generic import TemplateView
from django.shortcuts import render


class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class ResultPage(TemplateView):
    template_name = 'result.html'

class CaseList(TemplateView):
    template_name = 'case_list.html'


class Homepage(TemplateView):
    template_name = 'index.html'
