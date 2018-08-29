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


class ImageBlock(ImageChooserBlock):
    class Meta:
        template='projects/blocks/image_block.html'

class ParagraphBlock(blocks.RichTextBlock):
    class Meta:
        template='projects/blocks/paragraph_block.html'

class RowBlock(blocks.StreamBlock):

    paragraph_block = ParagraphBlock()
    image_block = ImageBlock()
    pull_quote_block = PullQuoteBlock()

    class Meta:
        template='projects/blocks/row_block.html'
        icon='list-ul'