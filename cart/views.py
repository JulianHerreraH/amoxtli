from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Book
from users.models import Profile
from .cart import Cart
from .forms import CartAddBookForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse




# Create your views here.


@require_POST
@login_required
def cart_add(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    form = CartAddBookForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(book = book, request =request)
    return HttpResponseRedirect(reverse('cart:cart_detail'))


def cart_remove(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    cart.remove(book)
    return HttpResponseRedirect(reverse('cart:cart_detail'))

def cart_detail(request):
    #book = request.GET.get("book")
    cart = Cart(request)
    books = Book.objects.all()
    totalPrice = 0
    length = 0
    print('-----------------------')
    for item in cart:
        print( item)
        book = item.get('book')
        if book in books:
            totalPrice = totalPrice + book.price
            length = length + 1
       
    print('-----------------------')
    currentlyLoggedUser = request.user
    userProfile = Profile.objects.get(user=currentlyLoggedUser.id)
    
    context = {
        'cart':cart,
        'userProfile':userProfile,
        'books': books,
        'totalPrice':totalPrice,
        'length':length
    }
    return render(request, 'cart/detail.html', context)