from django.db import models


class Sample(models.Model):
    attachment = models.FileField()


class Book(models.Model):
    """Records information about the books being sold in the bookstore chain."""
    author = models.CharField(max_length=255)          # Author name
    title = models.CharField(max_length=255)            # Book title
    description = models.TextField()                    # Book description
    thumbnail_url = models.CharField(max_length=500)     # URL to the book's cover image
    price = models.DecimalField(max_digits=8, decimal_places=2)  # Price, e.g. 19.99

    def __str__(self):
        return self.title


class Branch(models.Model):
    """Records information about branches of the bookstore chain."""
    branch_name = models.CharField(max_length=255)       # Name of the branch
    address = models.CharField(max_length=255)           # Street address
    city = models.CharField(max_length=100)               # City
    state = models.CharField(max_length=100)               # State
    zip = models.CharField(max_length=20)                  # Zip/postal code
    phone = models.CharField(max_length=20)                 # Contact phone number

    def __str__(self):
        return self.branch_name


class Inventory(models.Model):
    """Records book inventory at each branch. Book and Branch are foreign keys."""
    book = models.ForeignKey(Book, on_delete=models.CASCADE)      # Which book
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)  # Which branch carries it
    quantity = models.IntegerField()                               # How many copies in stock

    def __str__(self):
        return f"{self.book.title} @ {self.branch.branch_name} ({self.quantity})"