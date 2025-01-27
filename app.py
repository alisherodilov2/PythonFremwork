from core.routing import Router
from core.request import Request
from core.response import Response
from core.view import View

def handle_request(environ, start_response):
    request = Request(environ)
    router = Router()


    router.get('/hello', lambda: Response(View.render('<h1>Hello, World!</h1>', {})))
    router.get('/about', lambda: Response(View.render('<h1>About Page</h1>', {})))


    handler = router.resolve(request.environ['REQUEST_METHOD'], environ['PATH_INFO'])
    
    response = handler.render()


    start_response("200 OK", [("Content-Type", "text/html")])
    return [response.encode("utf-8")]

if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    # Run the WSGI server
    httpd = make_server('localhost', 8000, handle_request)
    print("Serving on http://localhost:8000")
    httpd.serve_forever()
