# Generated by Django 2.0 on 2018-05-18 21:48

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20180511_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='rss_feed',
            field=wagtail.core.fields.StreamField((('rss_feed', wagtail.core.blocks.StructBlock((('feed_url', wagtail.core.blocks.URLBlock()), ('number_of_posts', wagtail.core.blocks.IntegerBlock())))),), blank=True),
        ),
    ]
