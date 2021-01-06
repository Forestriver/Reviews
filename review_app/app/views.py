from aiohttp_boilerplate.views.create import CreateView
from aiohttp_boilerplate.views.list import ListView
from aiohttp_boilerplate.views.list import RetrieveView

from app import models
from app import schemas

# Endpont to retrieve data by id

class PostListView(RetrieveView):
    def get_model(self):
        return models.Post

    def get_schema(self):
        return schemas.PostSchema

    def review(self):
        result = self.get_model.get_by_id(id=2)
