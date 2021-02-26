from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
import datetime
from .forms import ResourceForm
from django.views.generic import FormView, DeleteView, DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin

from .models import Resource


class IndexView(ListView):
    template_name = 'journal_entries/index.html'
    model = Resource

    def get_queryset(self):
        return Resource.objects.order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = ResourceForm()
        return context

    def post(self, request):
        form = ResourceForm(data=request.POST)
        if form.is_valid():
            new_resource = form.save(commit=False)
            new_resource.pub_date = datetime.datetime.now()
            new_resource.save()

        return HttpResponseRedirect(reverse('journal_entries:index'))


class DetailView(DetailView):
    model = Resource
    template_name = 'journal_entries/detail.html'


class DeleteView(DeleteView):
    model = Resource
    success_url = reverse_lazy('journal_entries:index')


def create_resource_ajax(request):
    form = ResourceForm()
    context = {'form': form}
    html_form = render_to_string('journal_entries/partial_resource_create.html',
                                 context,
                                 request=request,
                                 )

    return JsonResponse({'html_form': html_form})
