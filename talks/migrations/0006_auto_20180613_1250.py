# Generated by Django 2.0.6 on 2018-06-13 16:50

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0005_auto_20180511_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='talk',
            name='hero',
        ),
        migrations.AddField(
            model_name='talk',
            name='banner',
            field=wagtail.core.fields.StreamField((('banner', wagtail.core.blocks.StructBlock((('subject', wagtail.core.blocks.CharBlock(required=False)), ('alternate_title', wagtail.core.blocks.CharBlock(required=False))))),), default=''),
            preserve_default=False,
        ),
    ]
