from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
import datetime
from .forms import ResourceForm
from django.views import generic
from django.views.generic.edit import FormView, FormMixin

from .models import Resource


class IndexView(generic.FormView):
    template_name = 'journal_entries/index.html'
    resource_list = Resource.objects.order_by('-pub_date')[:10]
    form_class = ResourceForm
    model = Resource

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({'resource_list': self.resource_list})
        return context

    def post(self, request, *args, **kwargs):
        form = ResourceForm(data=request.POST)
        if form.is_valid():
            new_resource = form.save(commit=False)
            new_resource.pub_date = datetime.datetime.now()
            new_resource.save()

        return HttpResponseRedirect(reverse('journal_entries:index'))


class DetailView(generic.DetailView):
    model = Resource
    template_name = 'journal_entries/detail.html'

