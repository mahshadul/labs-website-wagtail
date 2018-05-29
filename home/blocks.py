from django.db import models

from wagtail.core import blocks
import feedparser

class HeroBlock(blocks.StructBlock):
    subject = blocks.CharBlock(required=False)
    alternate_title = blocks.CharBlock(required=False)
    class Meta:
        icon = "placeholder"
        template = "home/blocks/hero.html"


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


class RSSBlock(blocks.StructBlock):
    feed_url = blocks.URLBlock()
    number_of_posts = blocks.IntegerBlock()

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context['posts'] = feedparser.parse(value['feed_url']).entries[:value['number_of_posts']]
        print(context['posts'])
        return context

    class Meta:
        icon = "code"
        template = "home/blocks/rss_feed.html"
