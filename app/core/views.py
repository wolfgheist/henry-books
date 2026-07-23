from django.shortcuts import render, get_object_or_404
from .models import Book, Branch, Inventory

# Create your views here.

def home(request):
    context = {
        "book_count": Book.objects.count(),
        "branch_count": Branch.objects.count(),
    }
    return render(request, "core/home.html", context)


def book_list(request):
    books = Book.objects.all().order_by("title")
    return render(request, "core/books.html", {"books": books})


def branch_list(request):
    branches = Branch.objects.all().order_by("branch_name")
    return render(request, "core/branches.html", {"branches": branches})


def branch_inventory(request, pk):
    branch = get_object_or_404(Branch, pk=pk)
    inventory = Inventory.objects.filter(branch=branch).select_related("book")
    return render(request, "core/branch_inventory.html", {
        "branch": branch,
        "inventory": inventory,
    })