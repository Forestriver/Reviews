from aiohttp_boilerplate.views.create import CreateView
from aiohttp_boilerplate.views.list import ListView
from aiohttp import web

from app import models
from app import schemas

# Endpont to retrieve data by id
class PostListView(ListView):
    def review(self):
        result = models.Post()
        result.get_by_id(id=3)
        return self.id
