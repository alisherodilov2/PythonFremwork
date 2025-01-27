class Request:
    def __init__(self, environ):
        self.environ = environ

    def get_param(self, name):
        return self.environ.get(name)

    def get_all_params(self):
        return self.environ
