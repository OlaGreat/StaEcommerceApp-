class Cart():
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('session.key')