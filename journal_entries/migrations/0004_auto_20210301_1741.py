# Generated by Django 3.1.7 on 2021-03-01 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal_entries', '0003_auto_20210301_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='framework',
            field=models.CharField(max_length=50, verbose_name='Framework/Technology'),
        ),
    ]
