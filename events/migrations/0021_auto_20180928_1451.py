# Generated by Django 2.0 on 2018-09-28 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0020_event_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Event end date'),
        ),
    ]
