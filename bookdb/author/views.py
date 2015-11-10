from django.shortcuts import render
from author.models import Author
from django.shortcuts import render_to_response
# Create your views here.

def index(request, AuthorID):
    Author_list = Author.objects.all()
    for author in Author_list:
        if author.AuthorID == AuthorID:
            return render_to_response('Author.html',{'author':author})
