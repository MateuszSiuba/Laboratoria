from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book

# 1. Lista książek + Filtrowanie
class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        queryset = super().get_queryset()
        # Pobieramy parametr 'author' z paska adresu (np. ?author=Lem)
        author_query = self.request.GET.get('author')
        if author_query:
            # Filtrujemy wyniki (icontains = zawiera frazę, bez względu na wielkość liter)
            queryset = queryset.filter(author__icontains=author_query)
        return queryset

# 2. Dodawanie książki
class BookCreateView(CreateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'author', 'publication_date']
    success_url = reverse_lazy('book_list')

# 3. Edycja książki
class BookUpdateView(UpdateView):
    model = Book
    template_name = 'books/book_form.html'
    fields = ['title', 'author', 'publication_date']
    success_url = reverse_lazy('book_list')

# 4. Usuwanie książki
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')