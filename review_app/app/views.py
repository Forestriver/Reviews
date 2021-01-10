from aiohttp_boilerplate.views.create import CreateView
from aiohttp_boilerplate.views.list import ListView
from aiohttp_boilerplate.views.retrieve import RetrieveView

from app import models
from app import schemas


# Endpoint to access the whole list of reviews.
class PostListView(ListView):
    def get_model(self):
        return models.Post

    def get_schema(self):
        return schemas.PostSchema

# Endpont to retrieve data by id
class ListById(RetrieveView):
    def get_model(self):
        return models.Post

    async def before_get(self):
        self.where ='id=2'
