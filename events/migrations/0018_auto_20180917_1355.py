# Generated by Django 2.0 on 2018-09-17 17:55

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_auto_20180917_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventfeaturedtalk',
            name='event',
        ),
        migrations.AddField(
            model_name='eventfeaturedtalk',
            name='event',
            field=modelcluster.fields.ParentalKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='event_talks', to='events.Event'),
            preserve_default=False,
        ),
    ]