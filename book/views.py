from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from django.views import generic
from .models import Book, Publisher, Author
from . import forms
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied


class AuthorList(generic.ListView):
    template_name = 'authors/author_list.html'
    context_object_name = 'authors'
    paginate_by = 10

    def get_queryset(self):
        return Author.objects.all()


class AuthorDetail(generic.DetailView):
    template_name = 'authors/author_detail.html'
    context_object_name = 'author'

    def get_object(self, queryset=None):
        return get_object_or_404(Author, pk=self.kwargs.get('id'))


@login_required()
def author_create(request):
    if request.method == 'POST':
        form = forms.AuthorForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.owner = request.user
            data.save()
            return redirect(reverse('book:author_list'))

    else:
        form = forms.AuthorForm()
    return render(request, 'authors/author_create.html', context=dict(form=form))


@login_required()
def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = forms.AuthorForm(data=request.POST, instance=author)
        if form.is_valid():
            if not author.owner == request.user:
                return HttpResponseForbidden("You must be owner!!")
                # raise PermissionDenied("You must be owner!!")
            form.save()
            return redirect(reverse('book:author_list'))
    else:
        form = forms.AuthorForm(instance=author)
    return render(request, 'authors/author_create.html', context=dict(form=form))


@login_required()
def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        if not author.owner == request.user:
            return HttpResponseForbidden("You must be owner!!")
        author.delete()
        return redirect(reverse('book:author_list'))
    else:
        return render(request, 'authors/author_delete.html')


class PublisherList(generic.ListView):
    template_name = 'publishers/publisher_list.html'
    context_object_name = 'publishers'
    paginate_by = 10

    def get_queryset(self):
        return Publisher.objects.all()


class PublisherCreate(generic.CreateView):
    template_name = 'publishers/publisher_create.html'
    model = Publisher
    success_url = '/book/publishers/'
    form_class = forms.PublisherForm
    context_object_name = 'form'
    #fields = ['name', 'address', 'city',
    #          'country', 'website', 'description', ]

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PublisherCreate, self).form_valid(form)


class PublisherUpdate(generic.UpdateView):
    template_name = 'publishers/publisher_create.html'
    model = Publisher
    success_url = '/book/publishers/'
    form_class = forms.PublisherForm
    context_object_name = 'form'
    pk_url_kwarg = 'pk'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(pk=self.kwargs.get('pk'))

    def form_valid(self, form):
        if not self.get_object().owner == self.request.user:
            return HttpResponseForbidden("you must be owner")
        form.save()
        return redirect(reverse('book:publisher_list'))


class PublisherDelete(generic.DeleteView):
    template_name = 'publishers/publisher_delete.html'
    model = Publisher

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(pk=self.kwargs.get('pk'))

    def post(self, request, *args, **kwargs):
        if not self.get_object().owner == self.request.user:
            return HttpResponseForbidden("you must be owner")
        self.get_object().delete()
        return redirect(reverse('book:publisher_list'))


class BookList(generic.ListView):
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_queryset(self):
        return Book.objects.all()


class BookCreate(generic.CreateView):
    template_name = 'books/book_create.html'
    model = Book
    context_object_name = 'book'
    form_class = forms.BookForm
    success_url = '/book/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BookCreate, self).form_valid(form)


class BookUpdate(generic.UpdateView):
    template_name = 'books/book_create.html'
    model = Book
    context_object_name = 'form'
    form_class = forms.BookForm

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(pk=self.kwargs.get('pk'))

    def form_valid(self, form):
        if not self.get_object().owner == self.request.user:
            return HttpResponseForbidden("you must be owner")
        form.save()
        return redirect(reverse('book:book_list'))


class BookDelete(generic.DeleteView):
    template_name = 'books/book_delete.html'
    model = Book

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(pk=self.kwargs.get('pk'))

    def post(self, request, *args, **kwargs):
        if not self.get_object().owner == self.request.user:
            return HttpResponseForbidden("you must be owner")
        self.get_object().delete()
        return redirect(reverse('book:book_list'))
