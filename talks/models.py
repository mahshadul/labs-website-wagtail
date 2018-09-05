from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page

from home.models import BasePageWithHero

class TalkList(Page):
    subpage_types = ['talks.Talk']


class Talk(BasePageWithHero):
    
    author = models.CharField(max_length=200)
    video_id = models.CharField(max_length=50)
    exerpt = RichTextField(help_text="Summary for list view, not displayed in detail view")
    date = models.DateField("Talk date")
    location = models.CharField(max_length=100)


    content_panels = BasePageWithHero.content_panels + [
        FieldPanel('author', classname='full'),
        FieldPanel('video_id', classname='full'),
        FieldPanel('exerpt', classname='full'),
        FieldPanel('date', classname='full'),
        FieldPanel('location', classname='full'),
    ]

    parent_page_types = ['talks.TalkList']
