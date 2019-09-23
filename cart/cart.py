from decimal import Decimal
from django.conf import settings
from store.models import Book

class Cart(object):
    total = 0
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, book, request):
        book_id = str(book.id)
        user = (book.publishedBy.id)
        if book_id not in self.cart and user != request.user.id:
           
            self.cart[book_id] = {'price':str(book.price)}
            self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, book):
        book_id = str(book.id)
        if book_id in self.cart:
            del self.cart[book_id]
            self.save()

    def __iter__(self):
        books_ids = self.cart.keys()
        books = Book.objects.filter(id__in=books_ids)
        for book in books:
            self.cart[str(book.id)]['book'] = book
        
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            yield item

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
    
  