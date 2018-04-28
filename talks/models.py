from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page

from home.models import BasePageWithHero


class TalkList(Page):
#    subpage_types = ['talks.Talk']
    pass


class Talk(BasePageWithHero):

    # Database fields

    author = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    video_id = models.CharField(max_length=50)
    body = RichTextField()
    content_panels = BasePageWithHero.content_panels + [
        FieldPanel('author', classname='full'),
        FieldPanel('description', classname='full'),
        FieldPanel('video_id', classname='full'),
        FieldPanel('body', classname='full')
    ]

#    parent_page_types = ['talks.TalkList']
