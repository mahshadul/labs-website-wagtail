from django.db import models

from wagtail.core import blocks
import feedparser

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

