# Generated by Django 2.0 on 2018-09-05 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_remove_event_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]