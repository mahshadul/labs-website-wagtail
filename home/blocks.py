from django.db import models

from wagtail.core import blocks
import feedparser

from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.fields import StreamField


class FAIconLinkBlock(blocks.StructBlock):
    icon = blocks.CharBlock(help_text="Font Awesome icon name")
    url = blocks.URLBlock(help_text="URL to link to")
    class Meta:
        icon = "link"
        template = "home/blocks/icon_link.html"


class DetailBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    text = blocks.RichTextBlock(blank=True)

    class Meta:
        icon = "user"
        template = "home/blocks/detail.html"


class PullQuoteBlock(blocks.BlockQuoteBlock):
    class Meta:
        template='projects/blocks/pull_quote_block.html'

class GalleryBlock(blocks.ListBlock):
    class Meta:
        template='projects/blocks/gallery_block.html'
        icon='image'

class ParagraphBlock(blocks.StructBlock):
    text= blocks.RichTextBlock()
    image = ImageChooserBlock(required=False)
    class Meta:
        template='projects/blocks/paragraph_block.html'
        icon='pilcrow'