from store.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}


        self.cart = cart

    def add(self, product):
        
        product_id = str(product.id)

        if product_id in self.cart:
            pass
        
        else:
            print(self.cart)
            self.cart[product_id] = {'price': str(product.price)}

        self.session.modified = True 



    def __len__(self):
        return len(self.cart)
    
    def delete(self, product_id):

        id = str(product_id)

        self.cart.pop(id)

        self.session.modified = True 
        

    def get_products(self):
        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=product_ids)

        return products


        