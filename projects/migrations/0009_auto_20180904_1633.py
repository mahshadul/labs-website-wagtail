# Generated by Django 2.0 on 2018-09-04 20:33

from django.db import migrations
import home.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20180904_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpage',
            name='body',
            field=wagtail.core.fields.StreamField((('paragraph_block', wagtail.core.blocks.StructBlock((('text', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))))), ('pull_quote_block', home.blocks.PullQuoteBlock()), ('gallery_block', home.blocks.GalleryBlock(wagtail.images.blocks.ImageChooserBlock())), ('content_highlight_block', wagtail.core.blocks.StructBlock((('text', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)))))), blank=True),
        ),
    ]
