from __future__ import annotations
from typing import TypeVar

from pydantic import BaseModel


Hint = tuple[str, str]


class Widget(BaseModel):
    # common widget options
    name: str
    label: str | None = None # if None, name will be sluggified
    required: bool = False
    hint: Hint | None = None

    def dict(self, exclude_none=True, **kwargs):
        return super().dict(exclude_none=exclude_none, **kwargs)


W = TypeVar('W', bound=Widget)
Widgets = list[W]


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
    summary: str | None = None

class SelectWidget(Widget):
    widget: str = 'select'
    options: list[str]
    default: list[str]

class ObjectWidget(Widget):
    widget: str = 'object'
    summary: str | None = None
    collapsed: bool | None = None
    fields: Widgets

class ImageWidget(Widget):
    widget: str = 'image'
    choose_url: bool | None = None

class RelationWidget(Widget):
    widget: str = 'relation'
    multiple: bool | None = None
    collection: str
    search_fields: list[str]
    value_field: str
    display_fields: list[str] | None = None

class DateTimeWidget(Widget):
    widget: str = 'datetime'
    date_format: str | None = None
    time_format: bool | None = None