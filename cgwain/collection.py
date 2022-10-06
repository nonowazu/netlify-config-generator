from typing import Any

from pydantic import BaseModel

from cgwain.types import Widgets

    

class Collection(BaseModel):
    """Represents a collection in the netlify editor.
    For information on collections, see https://www.netlifycms.org/docs/configuration-options/#collections
    """
    # TODO: all commented fields with TodoType need to be filled in
    name: str
    # identifier_field: TodoType = ???
    label: str | None = None
    label_singular: str | None = None
    description: str | None = None
    # publish: TodoType = ???
    # hide: TodoType = ???
    delete: bool | None = None # set to true to allow deleting new files; defaults to true
    # extension: TodoType = ???
    # format: TodoType = ???
    # frontmatter_delimeter: TodoType = ???
    # slug: TodoType | None = None
    # preview_path: TodoType = ???
    # preview_path_date_field: TodoType = ???
    fields: Widgets
    # editor: TodoType = ???
    # summary: TodoType = ???
    # sortable_fields: TodoType = ???
    # view_filters: TodoType = ???
    # view_groups = TodoType = ???

    def __repr__(self) -> str:
        return f'<Collection:{self.__class__.__name__}>'

    def dict(self, exclude_none=True, **kwargs):
        return super().dict(exclude_none=exclude_none, **kwargs)

class FolderCollection(Collection):
    folder: str
    # filter: TodoType = ???
    create: bool | None = None # set to true to allow creating new files; defaults to false

class FileCollection(Collection):
    # files: TodoType = ???
    pass


class FileEntry:
    ...


class FileCollection:
    ...
