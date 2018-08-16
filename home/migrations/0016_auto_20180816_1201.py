# Generated by Django 2.0 on 2018-08-16 16:01

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20180613_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='about_us',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='banner',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='rss_feed',
        ),
        migrations.AddField(
            model_name='homepage',
            name='about_us_text',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='about_us_title',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='homepage',
            name='alternate_title',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='homepage',
            name='feed_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='number_of_posts',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='subject',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]