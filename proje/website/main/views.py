from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm


# Kitapları listele
class BookListView(ListView):
    model = Book
    template_name = 'main/book_list.html'
    context_object_name = 'books'

# Kitap detaylarını göster
class BookDetailView(DetailView):
    model = Book
    template_name = 'main/book_detail.html'
    context_object_name = 'book'

# Yeni kitap ekle
class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'main/book_form.html'
    success_url = reverse_lazy('book_list')

# Kitabı sil
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'main/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')
