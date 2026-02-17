class Handler:
    def __init__(self, next_handler=None):
        self.next = next_handler

    def handle(self, request):
        raise NotImplementedError()


class RequiredFieldHandler(Handler):
    def handle(self, request):
        if not request.get("name"):
            return ["name is required"]
        if self.next:
            return self.next.handle(request)
        return []


class EmailHandler(Handler):
    def handle(self, request):
        if "@" not in request.get("email", ""):
            return ["invalid email"]
        if self.next:
            return self.next.handle(request)
        return []
    
    # Factory
    def build_chain():
    return RequiredFieldHandler(
        EmailHandler()
    )