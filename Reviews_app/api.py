import aiohttp_jinja2
import asyncio
import aiohttp
from aiohttp import web


aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader('/templates'))

routes = web.RouteTableDef()


"""home page with input form to check for reviews"""
@routes.get('/')
@aiohttp_jinja2.template("home.html")
async def search_reviews(request)
    return {}


""" Route getting the data found"""
@routes.post('/scrape')
async def collect_reviews(request)
    request_data = await request.form()
    scraper = Scraper()
    scraper.run(request_data["Reviews_found"])
    return "success"


app = web.Application()
app.router.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app)
