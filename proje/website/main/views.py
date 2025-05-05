from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm  # forms.py'de BookForm sınıfı tanımlanmalı

# Kitapları listele
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

# Kitap detaylarını göster
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

# Yeni kitap ekle
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

# Kitabı sil
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})
