from django.db import models
from django.contrib import admin

# Create your models here.
class Book(models.Model):
    class Meta:
        verbose_name = 'books'
        verbose_name_plural = verbose_name
    ISBN          = models.CharField('ISBN(PK)',max_length=13,unique=True)
    Title           = models.CharField('Title',max_length=200)
    AuthorID          = models.CharField('AuthorID(FK)',max_length=60)
    Price           = models.CharField('Price',max_length=60,blank=True)
    Publisher       = models.CharField('Publisher',max_length=200,blank=True)
    PublishDate         = models.CharField('PublishDate',max_length=60,blank=True)
    Summary        = models.TextField ('Summary',blank=True,max_length=2000)
	
class BookIssue(admin.ModelAdmin):
	list_display = ('ISBN','Title','AuthorID','Price','Publisher','PublishDate','Summary')
	
	# def __unicode__(self):
        # return str(self.title)
		
admin.site.register(Book,BookIssue)