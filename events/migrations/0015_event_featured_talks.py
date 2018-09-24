# Generated by Django 2.0 on 2018-09-17 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0012_talk_description'),
        ('events', '0014_event_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='featured_talks',
            field=models.ManyToManyField(to='talks.Talk'),
        ),
    ]