# Generated by Django 2.0 on 2018-08-30 12:51

from django.db import migrations
import home.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20180822_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='body',
            field=wagtail.core.fields.StreamField((('paragraph_block', wagtail.core.blocks.StructBlock((('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))))), ('pull_quote_block', home.blocks.PullQuoteBlock()), ('gallery_block', home.blocks.GalleryBlock(wagtail.images.blocks.ImageChooserBlock()))), blank=True),
        ),
    ]
