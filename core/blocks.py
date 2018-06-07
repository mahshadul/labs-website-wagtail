from wagtail.core import blocks

class IframeBlock(blocks.StructBlock):
    source = blocks.URLBlock()
    height = blocks.IntegerBlock(min_value=0)
    width = blocks.IntegerBlock(min_value=0)
    extra_attributes = blocks.CharBlock(required=False)

    class Meta:
        icon = "code"
        template = "core/blocks/iframe.html"