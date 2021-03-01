from django.db import models
import django_tables2 as tables
from django.utils.safestring import mark_safe
from django_tables2 import A, TemplateColumn
from django.utils.html import format_html


class Resource(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    link = models.URLField()
    language = models.CharField(max_length=50)
    framework = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date added')

    def __str__(self):
        return self.title


class ResourceTable(tables.Table):
    class Meta:
        model = Resource
        template_name = "journal_entries/resource_list.html"
        sequence = ('title', 'language', 'framework', 'pub_date')
        exclude = ('id', 'description', 'link')

    def render_title(self, record, value):
        resource_title = value
        resource_link = record.link
        return format_html(f"<a href='{resource_link}' id='resource_title'>  {resource_title} </a>")

    def render_pub_date(self, value):
        return value.strftime('%d %b %y')

    edit = TemplateColumn(template_name='journal_entries/edit_button.html', verbose_name='')
    delete = TemplateColumn(template_name='journal_entries/delete_button.html', verbose_name='')


class Topic(models.Model):
    tag = models.CharField(max_length=20)
    resources = models.ManyToManyField(Resource)

    def __str__(self):
        return self.tag
