class Router:
    def __init__(self):
        self.routes = {}

    def add(self, method, path, handler):
        self.routes[(method, path)] = handler

    def get(self, path, handler):
        self.add("GET", path, handler)

    def post(self, path, handler):
        self.add("POST", path, handler)

    def resolve(self, method, path):
        handler = self.routes.get((method, path))
        if handler:
            return handler()
        else:
            return "404 Not Found"
