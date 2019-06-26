from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import CalcForm


class CalcView(TemplateView):
    template_name = "app/calc.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if request.GET:
            form = CalcForm(request.GET)
            context['form'] = form
            if form.is_valid():
                common_result = form.cleaned_data['initial_fee'] + \
                                (form.cleaned_data['initial_fee'] * form.cleaned_data['rate'] / 100)
                context['common_result'] = round(common_result, 2)
                result = common_result / form.cleaned_data['months_count']
                context['result'] = round(result, 2)
        else:
            context['form'] = CalcForm()
        return self.render_to_response(context)
