from django.shortcuts import render, get_object_or_404
from .models import Book, Genre, Subject
from users.models import Profile
from .forms import BookForm
from django.views.generic import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from cart.forms import CartAddBookForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse



# Create your views here.

#View for Home page
def home(request):
    booksFirst = Book.objects.filter(datePosted__isnull=False).order_by('datePosted')
    booksLast = Book.objects.filter(datePosted__isnull=False).order_by('-datePosted')
    booksPrice = Book.objects.order_by('price')
   
    context = {
        'booksFirst': booksFirst,
        'booksPrice': booksPrice,
        'booksLast': booksLast,
    }
    return render(request, 'store/home.html', context)

#View for about page
def about(request):
    return render(request, 'store/about.html', {'title': 'Nosotros'})

#View for Frequently Asked Questions
def faq(request):
    return render(request, 'store/faq.html', {'title': 'FAQ'})

#View for Quality Guidelines
def guides(request):
    return render(request, 'store/guidelines.html', {'title': 'Guía de Calidad'})

#View for contact and social info
def contact(request):
    return render(request, 'store/contact.html',{'title': 'Contacto'})

#View for subjects and books
def book_subject_list(request, subject_slug=None):
    subject = None
    subjects = Subject.objects.all()
    books = Book.objects.order_by('price')
    if subject_slug:
        subject = get_object_or_404(Subject, slug=subject_slug)
        books = Book.objects.filter(subject=subject)

    context = {
        'subject': subject,
        'subjects': subjects,
        'books': books
    }
    return render(request, 'store/subjects.html', context)

#View for genres and books    
def book_genre_list(request, genre_slug=None):
    genre = None
    genres = Genre.objects.all()
    books = Book.objects.order_by('price')
    print(genres)
    if genre_slug:
        genre = get_object_or_404(Genre, slug=genre_slug)
        books = Book.objects.filter(genre=genre)

    context = {
        'genre': genre,
        'genres': genres,
        'books': books
    }
    return render(request, 'store/genres.html', context)


#View for specific book
@login_required
def book_detail(request, pk):
    currentlyLoggedUser = request.user
    userProfile = Profile.objects.get(user=currentlyLoggedUser.id)
    book = get_object_or_404(Book, pk=pk)
    books = Book.objects.order_by('price')
    
    context = {
        'book': book,
        'books': books,
        'userProfile': userProfile,
       
    }
    return render(request, 'store/detail.html', context)

#Class view for book creation
class bookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    #fields = ['title', 'price', 'author', 'publisher', 'description', 'genre', 'subject', 'quality', 'image']
    form_class = BookForm

    def form_valid(self, form):
        form.instance.publishedBy = self.request.user
        return super().form_valid(form)

#Class view for book update
class bookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['title', 'price', 'author', 'publisher', 'description', 'genre', 'subject', 'quality', 'image']

    def form_valid(self, form):
        form.instance.publishedBy = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        book = self.get_object()
        if self.request.user == book.publishedBy:
            return True
        return False

#Class view for book delete
class bookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    success_url = '/'
    def test_func(self):
        book = self.get_object()
        if self.request.user == book.publishedBy:
            return True
        return False

def search(request):
   
    query = request.GET.get('q')
    
    if query:
        results = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query)
            | Q(publisher__icontains=query) | Q(genre__name__icontains=query) 
            | Q(subject__name__icontains=query)).order_by('price')
        context = {
            'results': results
        }
    else:
        return HttpResponseRedirect(reverse('store:store-home'))  
    

    
    return render(request, 'store/search.html', context)



       




