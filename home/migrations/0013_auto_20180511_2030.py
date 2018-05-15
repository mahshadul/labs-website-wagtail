# Generated by Django 2.0.5 on 2018-05-11 20:30

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20180511_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='featured',
            field=wagtail.core.fields.StreamField((('event_featured', wagtail.core.blocks.PageChooserBlock(target_model=['events.Event'])), ('talk_featured', wagtail.core.blocks.PageChooserBlock(target_model=['talks.Talk'])), ('showcase_featured', wagtail.core.blocks.PageChooserBlock(target_model=['showcase.ShowcasePage'])), ('event', wagtail.core.blocks.PageChooserBlock(target_model=['events.Event'])), ('talk', wagtail.core.blocks.PageChooserBlock(target_model=['talks.Talk'])), ('showcase', wagtail.core.blocks.PageChooserBlock(target_model=['showcase.ShowcasePage'])))),
        ),
    ]
