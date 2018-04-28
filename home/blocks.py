from django.db import models

from wagtail.core.blocks import StructBlock, CharBlock, RichTextBlock

class HeroBlock(StructBlock):
    subject = CharBlock(required=False)
    class Meta:
        icon = "user"
        template = "home/blocks/hero.html"


class DetailBlock(StructBlock):
    title = CharBlock(required=False)
    text = RichTextBlock(blank=True)

    class Meta:
        icon = "user"
        template = "home/blocks/detail.html"