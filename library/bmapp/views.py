from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from .models import Book
# Create your views here.
def homeView(request):
    books = Book.objects.all().order_by('-id')
    recent_books = books[:6]
    
    # Calculate statistics
    total_books = books.count()
    
    # Get unique authors (excluding empty/None values)
    unique_authors = books.exclude(author__isnull=True).exclude(author__exact='').values_list('author', flat=True).distinct()
    authors_count = len(unique_authors)
    
    # Calculate total collection value
    total_value = sum(book.price for book in books if book.price)
    
    return render(request, "home.html", {
        "books": books, 
        "recent_books": recent_books,
        "authors": unique_authors,
        "total_value": total_value
    })
def helloView(request):
    search_query = request.GET.get('search', '')
    if search_query:
        # Search for books by title (case-insensitive)
        books = Book.objects.filter(title__icontains=search_query).order_by('-id')
    else:
        books = Book.objects.all().order_by('-id')
    return render(request,"viewbook.html",{"books":books, "search_query":search_query})

def addBookView(request):
    return render(request,"addbook.html")


def addBook(request):
    if request.method=="POST":
        t=request.POST["title"]
        a=request.POST["author"]
        p=request.POST["price"]
        print(t,a,p)
        book=Book()
        book.title=t
        book.price=p
        book.author=a
        book.save()
        return HttpResponseRedirect('/')

def editBook(request):
    if request.method=="POST":
        t=request.POST["title"]
        a=request.POST["author"]
        p=request.POST["price"]
        
        book=Book.objects.get(id=request.POST['bid'])
        book.title=t
        book.author=a
        book.price=p
        book.save()
        return HttpResponseRedirect('/')


def editBookView(request):
    book=Book.objects.get(id=request.GET['bookid'])
    print(book)
    return render(request,"edit-book.html",{"book":book})

def deleteBookView(request):
    book=Book.objects.get(id=request.GET['bookid'])
    book.delete()
    return HttpResponseRedirect('/')

