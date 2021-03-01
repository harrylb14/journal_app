from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from .forms import ResourceForm
from django.views.generic import FormView, DeleteView, DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin
from django.core.paginator import Paginator
import django_tables2 as tables

from .models import Resource, ResourceTable


class IndexView(tables.SingleTableView):
    template_name = 'journal_entries/index.html'
    model = Resource

    def get_queryset(self):
        return Resource.objects.order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        form = ResourceForm()
        table = ResourceTable(self.get_queryset())

        context['form'] = form
        context['table'] = table

        return context

    def post(self, request):
        form = ResourceForm(data=request.POST)
        if form.is_valid():
            new_resource = form.save(commit=False)
            new_resource.pub_date = timezone.now()
            new_resource.save()

        return HttpResponseRedirect(reverse('journal_entries:index'))


class TableView(tables.SingleTableView):
    table_class = ResourceTable
    queryset = Resource.objects.order_by('-pub_date')
    template_name = 'resource_table.html'


def create_resource_ajax(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
    else:
        form = ResourceForm()

    return save_resource_form(request, form, 'journal_entries/partial_resource_create.html')


def update_resource_ajax(request, resource_id):
    resource = get_object_or_404(Resource, pk=resource_id)

    if request.method == 'POST':
        form = ResourceForm(request.POST, instance=resource)
    else:
        form = ResourceForm(instance=resource)

    return save_resource_form(request, form, 'journal_entries/partial_resource_update.html')


def delete_resource_ajax(request, resource_id):
    resource = get_object_or_404(Resource, pk=resource_id)
    data = dict()
    if request.method == 'POST':
        resource.delete()
        data['form_is_valid'] = True
        resource_list = Resource.objects.all()
        data['html_resource_list'] = render_to_string('journal_entries/partial_resource_list.html', {
            'resource_list': resource_list
        })
    else:
        context = {'resource': resource}
        data['html_form'] = render_to_string('journal_entries/partial_resource_delete.html',
                                             context,
                                             request=request,
                                             )

    return JsonResponse(data)


def save_resource_form(request, form, template_name):
    data = dict()

    if request.method == 'POST':
        if form.is_valid():
            new_resource = form.save(commit=False)

            if new_resource.pub_date is None:
                new_resource.pub_date = timezone.now()

            new_resource.save()

            data['form_is_valid'] = True
            resource_list = Resource.objects.all().order_by('-pub_date')
            data['html_resource_list'] = render_to_string('journal_entries/partial_resource_list.html', {
                'resource_list': resource_list
            })

        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string(template_name,
                                         context,
                                         request=request,
                                         )

    return JsonResponse(data)


def paginate(request):
    model = Resource.objects.order_by('-pub_date')
    number_of_resources = 2
    paginator = Paginator(model, number_of_resources)
    if request.method == 'POST':
        page_n = request.POST.get('page_n', None)
        results = list(paginator.page(page_n).object_list())
        return JsonResponse({'results': results})

    return HttpResponseRedirect(reverse('journal_entries:index'))