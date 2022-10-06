# GCWAIN - (Netlify) config generator without an interesting name

## Example:

```python
import yaml

from cgwain.collection import FolderCollection
from cgwain.widgets import ColorWidget, ListWidget, MarkdownWidget, NumberWidget, StringWidget
from cgwain.types import Widgets

class RoleMetadata(FolderCollection):
    fields: Widgets = [
        StringWidget(label='Short name', name='title'),
        StringWidget(label='Role name', name='name'),
        NumberWidget(label='Display order', name='order'),
        ColorWidget(label='Color', name='color'),
        StringWidget(label='Icon', name='icon'),
        StringWidget(label='Link', name='role_link'),
        MarkdownWidget(label='Description', name='role_text_md'),
        ListWidget(
            label='Job Information',
            name='jobs',
            fields=[
                StringWidget(label='Name', name='name'),
                StringWidget(label='Link', name='job_link'),
                StringWidget(label='Icon', name='icon'),
            ]
        )
    ]

r = RoleMetadata(label='Role metadata', name='role-data', folder='data/roles/')
print(yaml.dump(r.dict()))
```