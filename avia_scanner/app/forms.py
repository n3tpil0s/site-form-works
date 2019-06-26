from django import forms
from django.forms.widgets import SelectDateWidget
from django.urls import reverse_lazy
from .widgets import AjaxInputWidget
from .models import City


class SearchTicket(forms.Form):
    from_city = forms.CharField(
        widget=AjaxInputWidget(url=reverse_lazy('cities_lookup')),
        label='Город отправления'
    )
    to_city = forms.ModelChoiceField(
        City.objects.all(),
        label='Город назначения'
    )
    date = forms.DateField(widget=SelectDateWidget)

