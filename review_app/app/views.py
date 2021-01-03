from aiohttp_boilerplate.views.create import CreateView
from aiohttp_boilerplate.views.list import ListView

from .models import Post
from .schemas import PostSchema


class PostListView(ListView):
    def get_model(self):
        return Post

    def get_schema(self):
        return PostSchema
