from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from account.models import Account


class Publisher(models.Model):
    owner = models.ForeignKey(Account, related_name='publisher', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=64, db_index=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=64, blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Author(models.Model):
    owner = models.ForeignKey(Account, related_name='author', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64, blank=True, null=True)
    email = models.EmailField(max_length=64, blank=True, null=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.first_name


class Book(models.Model):
    owner = models.ForeignKey(Account, related_name='book', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=46, db_index=True)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(blank=True, null=True)
    num_page = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('created_at',)
