from typing import Any

from pydantic import BaseModel

from cgwain.types import Widgets

    

class Collection(BaseModel):
    """Represents a collection in the netlify editor.
    For information on collections, see https://www.netlifycms.org/docs/configuration-options/#collections
    """
    # TODO: all commented fields with TodoType need to be filled in
    name: str
    """unique identifier for the collection, used as the key when referenced in other contexts (like the relation widget)"""
    # identifier_field: TodoType = ???
    label: str | None = None
    """label for the collection in the editor UI; defaults to the value of ``name``"""
    label_singular: str | None = None
    """singular label for certain elements in the editor; defaults to the value of ``label``"""
    description: str | None = None
    """optional text, displayed below the label when viewing a collection"""
    # publish: TodoType = ???
    # hide: TodoType = ???
    delete: bool | None = None
    """``False`` prevents users from deleting items in a collection; defaults to ``True``"""
    # extension: TodoType = ???
    # format: TodoType = ???
    # frontmatter_delimeter: TodoType = ???
    # slug: TodoType | None = None
    # preview_path: TodoType = ???
    # preview_path_date_field: TodoType = ???
    fields: Widgets
    """The fields option maps editor UI widgets to field-value pairs in the saved file.
    The order of the fields in your Netlify CMS config.yml file determines their order in the editor UI 
    and in the saved file."""
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
    """Represents a folder collection in the netlify editor.
    For information on Folder collections, see https://www.netlifycms.org/docs/collection-types#folder-collections"""
    folder: str
    # filter: TodoType = ???
    create: bool | None = None # set to true to allow creating new files; defaults to false

class File(Collection):
    """Represents an individual file in a File Collection"""
    file: str

class FileCollection(Collection):
    """Represents a file collection in the netlify editor.
    For information on File collections, see https://www.netlifycms.org/docs/collection-types#file-collections"""
    # This feels like a dirty hack, but it does (in theory) get rid of the normal field requirement
    fields: Widgets | None = None
    files: list[File]
