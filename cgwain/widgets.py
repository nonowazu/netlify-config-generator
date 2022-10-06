from pydantic import BaseModel

from cgwain.types import Hint, Widgets


class Widget(BaseModel):
    # common widget options
    name: str
    label: str | None = None # if None, name will be sluggified
    required: bool = False
    hint: Hint | None = None

    def dict(self, exclude_none=True, **kwargs):
        return super().dict(exclude_none=exclude_none, **kwargs)


class StringWidget(Widget):
    widget: str = 'string'


class NumberWidget(Widget):
    widget: str = 'number'


class ColorWidget(Widget):
    widget: str = 'color'


class MarkdownWidget(Widget):
    widget: str = 'markdown'


class ListWidget(Widget):
    widget: str = 'list'
    fields: Widgets