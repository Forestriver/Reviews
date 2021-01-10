from . import views

def setup_routes(app):
    app.router.add_route("GET", "/", views.PostListView)
    app.router.add_route("GET", "/review_id", views.ListById)
