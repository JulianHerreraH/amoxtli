from django.urls import path
from django.conf.urls import url
from . import views
from .views import bookCreateView, bookUpdateView, bookDeleteView

app_name = 'store'
urlpatterns = [
    path('', views.home, name='store-home'),
    path('about/', views.about, name='store-about'),
    path('faq/', views.faq, name='store-faq'),
    path('contact/', views.contact, name='store-contact'),
    path('genres/', views.book_genre_list, name='store-genres'),
    path('subjects/', views.book_subject_list, name='store-subjects'),
    path('book/new/', bookCreateView.as_view(), name='book-create'),
    path('guidelines/', views.guides, name='store-guide'),
    path('search/', views.search, name='store-search'),

    path('books/<int:pk>/update', bookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete', bookDeleteView.as_view(), name='book-delete'),

    path('subjects/<subject_slug>', views.book_subject_list, name='store-subjects-detail'),
    path('genres/<genre_slug>', views.book_genre_list, name='store-genres-detail'),
    path('books/<int:pk>', views.book_detail, name='store-detail'),
    
    #url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.book_detail, name='store-detail'),
    
]
