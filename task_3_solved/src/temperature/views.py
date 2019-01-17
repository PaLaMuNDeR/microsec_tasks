from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import FormMixin
from django.views.generic import DetailView, ListView
from .forms import UpdateValueForm
from .models import Temperature


class InboxView(LoginRequiredMixin, ListView):
    template_name = 'chat/inbox.html'


class TemperatureView(DetailView):
    template_name = 'temperature/temp.html'
    success_url = './'

    def get_queryset(self):
        return Temperature.objects.all()[:50]

    def get_object(self):
        values = Temperature.objects.all()[:50]
        if values is None:
            raise Http404
        return values


class TemperatureViewForm(FormMixin, DetailView):
    template_name = 'temperature/temp_update.html'
    form_class = UpdateValueForm
    success_url = './'

    def get_queryset(self):
        return Temperature.objects.all()[:50]

    def get_object(self):
        other_username  = self.kwargs.get("username")
        obj    = Temperature.objects.last()
        if obj == None:
            raise Http404
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        value = form.cleaned_data.get("value")
        Temperature.objects.create(value=value)
        return super().form_valid(form)


