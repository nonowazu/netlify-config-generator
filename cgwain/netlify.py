from __future__ import annotations

from pydantic import BaseModel

from cgwain.collection import Collection

# TODO: multiple inherited backends based off this
class Backend(BaseModel):
    """Represents backend config
    For more information, see https://www.netlifycms.org/docs/backends-overview/"""
    name: str
    """The backend type to use"""
    repo: str | None = None
    """Required for ``github``, ``gitlab``, and ``bitbucket`` backends; ignored by ``git-gateway``. Follows the pattern ``[org-or-username]/[repo-name]``."""
    branch: str | None = None
    """The branch where published content is stored. All CMS commits and PRs are made to this branch."""
    api_root: str | None = None
    """The API endpoint. Only necessary in certain cases, like with GitHub Enterprise or self-hosted GitLab."""
    # site_domain: TodoType = ???
    base_url: str | None = None
    """Sets the ``site_id`` query param sent to the API endpoint. Non-Netlify auth setups will often need to set this for local development to work properly."""
    auth_endpoint: str | None = None
    """Path to append to ``base_url`` for authentication requests. Optional."""
    cms_label_prefix: str | None = None
    """Pull (or Merge) Requests label prefix when using editorial workflow. Optional."""

    def dict(self, exclude_none=True, **kwargs):
        return super().dict(exclude_none=exclude_none, **kwargs)

class NetlifyConfig(BaseModel):
    """Represents a netlify-cms configuration file"""
    backend: Backend
    publish_mode: str | None = None # TODO: enum or some other validator?
    media_folder: str
    public_folder: str
    site_url: str | None = None
    show_preview_links: bool | None = None
    collections: list[Collection] = []
    local_backend: bool | None = None

    def dict(self, exclude_none=True, **kwargs):
        return super().dict(exclude_none=exclude_none, **kwargs)
