from typing import TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from cgwain.widgets import Widget

Hint = tuple[str, str]
W = TypeVar('W', bound='Widget')
Widgets = list[W]