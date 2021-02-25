from django.db import models


class Resource(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    link = models.URLField()
    language = models.CharField(max_length=50)
    framework = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date added')

    def __str__(self):
        return self.title


class Topic(models.Model):
    tag = models.CharField(max_length=20)
    resources = models.ManyToManyField(Resource)

    def __str__(self):
        return self.tag
