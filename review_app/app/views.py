from aiohttp_boilerplate.views.create import CreateView
from aiohttp_boilerplate.views.list import ListView
from aiohttp import web

from .models import Post
from .schemas import PostSchema

# Endpont to view data
class PostListView(ListView):
    def get_model(self):
        return Post

    def get_schema(self):
        return PostSchema

# Endpoint to add or update data
class UpdateView(ListView):
    async def post_review(self, request):
        data = await request.json()
        note = Post(id=data['id'], name=data['name'], content=data['content'])
        session.add(note)
        session.commit()

        return Response(status=201, body=self.resource.encode({
            'post_post': [
                {'id': note.id, 'name': note.name, 'content': note.content}

                    for note in session.query(Post)

                    ]
            }), content_type='application/json')
