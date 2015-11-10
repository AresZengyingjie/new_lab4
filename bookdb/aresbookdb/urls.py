"""aresbookdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'book.views.index'),
    url(r'^Authorbook/$', 'book.views.get_AuthorID'),
    url(r'^AddBook/$', 'book.views.AddBook'),
    url(r'^DelBook/(?P<bookISBN>\d*)/$', 'book.views.del_Book'),
    url(r'^UpdateBook/(?P<bookISBN>\d*)/$', 'book.views.UpdateBook'),
    url(r'^add_Book/$', 'book.views.add_Book'),
    url(r'^add_Author/$', 'book.views.add_Author'),
    url(r'^update_Book/(?P<bookISBN>\d*)/(?P<bookAuthorID>\d*)/$', 'book.views.update_Book'),
    url(r'^update_Author/(?P<authorAuthorID>\d*)/$', 'book.views.update_Author'),
    url(r'^Book/(?P<bookISBN>\d*)/$','book.views.BookInformation'),
	url(r'^Author/(?P<AuthorID>\d*)/$', 'author.views.index'), 
]
