from django.shortcuts import render
from book.models import Book
from author.models import Author
from django.shortcuts import render_to_response
# Create your views here.

def index(request):
    book_list = Book.objects.all()
    return render_to_response('index.html',{'book_list':book_list})

def BookInformation(request, bookISBN):
    book_list = Book.objects.all()
    for book in book_list:
        if book.ISBN == bookISBN:
            return render_to_response('book.html',{'book':book})
            
def get_AuthorID(request):
    AuthorName = request.GET.get('AuthorName','')
    Author_list = Author.objects.all()
    for author in Author_list:
        if author.Name == AuthorName:   
            book_list = Book.objects.filter(AuthorID = author.AuthorID);
            if book_list:
                return render_to_response('search_result.html',{'book_list':book_list})
    return render_to_response('SearchError.html')
    
def AddBook(request):
    return render_to_response('AddBook.html')
    
def add_Book(request):
    ISBN = request.GET.get('ISBN','')
    Title = request.GET.get('Title','')
    AuthorID = request.GET.get('AuthorID','')
    Price = request.GET.get('Price','')
    Publisher = request.GET.get('Publisher','')
    PublishDate = request.GET.get('PublishDate','')
    Summary = request.GET.get('Summary','')
    Book.objects.create(ISBN = ISBN, Title = Title, AuthorID = AuthorID, Price = Price, Publisher = Publisher, PublishDate = PublishDate, Summary = Summary)
    book_list = Book.objects.all()
    Author_list = Author.objects.filter( AuthorID = AuthorID)
    if Author_list:
        return render_to_response('add_result.html',{'book_list':book_list})
    else:
        return render_to_response('AddAuthor.html')
        
def add_Author(request):
    AuthorID = request.GET.get('AuthorID','')
    Name = request.GET.get('Name','')
    Age = request.GET.get('Age','')
    Country = request.GET.get('Country','')
    Author.objects.create(AuthorID = AuthorID, Name = Name, Age = Age, Country = Country)
    book_list = Book.objects.all()
    return render_to_response('add_result.html',{'book_list':book_list})
    
    
def del_Book(request, bookISBN):
    book_list = Book.objects.all()
    Book.objects.filter(ISBN = bookISBN).delete()
    return render_to_response('del_result.html',{'book_list':book_list})

def UpdateBook(request, bookISBN):
    book_list = Book.objects.all()
    for book in book_list:
        if book.ISBN == bookISBN:
            return render_to_response('UpdateBook.html',{'book':book})
  
def update_Book(request, bookISBN, bookAuthorID):
    AuthorID = request.GET.get('AuthorID','')
    Price = request.GET.get('Price','')
    Publisher = request.GET.get('Publisher','')
    PublishDate = request.GET.get('PublishDate','')
    Book.objects.filter(ISBN = bookISBN).update(AuthorID = AuthorID, Price = Price, Publisher = Publisher, PublishDate = PublishDate)
    Author_list = Author.objects.all()
    for author in Author_list:
        if author.AuthorID == bookAuthorID:
                return render_to_response('UpdateAuthor.html',{'author':author})
    
def update_Author(request, authorAuthorID):
    AuthorID = request.GET.get('AuthorID','')
    Name = request.GET.get('Name','')
    Age = request.GET.get('Age','')
    Country = request.GET.get('Country','')
    Author.objects.filter(AuthorID = authorAuthorID).update(AuthorID = AuthorID, Name = Name, Age = Age, Country = Country)
    book_list = Book.objects.all()
    return render_to_response('update_result.html',{'book_list':book_list})
#    