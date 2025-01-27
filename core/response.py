class Response:
    def __init__(self, content, status_code=200):
        self.content = content
        self.status_code = status_code

    def render(self):
        return f"HTTP/{self.status_code} {self.content}"
