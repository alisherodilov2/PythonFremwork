from core.routing import Router
from core.request import Request
from core.response import Response
from core.view import View

def handle_request(environ):
    request = Request(environ)
    router = Router()
    # Define routes
    router.get('/hello', lambda: Response(View.render('<h1>Hello World</h1>', {})))
    router.get('/about', lambda: Response(View.render('<h1>About</h1>', {})))
    
    # Resolve the route
    handler = router.resolve(request.environ['REQUEST_METHOD'], environ['PATH_INFO'])
    return handler.render()

def handle_404(request):
    return Response("404 Not Found", 404)
