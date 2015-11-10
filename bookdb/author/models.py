from django.db import models
from django.contrib import admin

# Create your models here.
class Author(models.Model):
    class Meta:
        verbose_name = 'Authors'
        verbose_name_plural = verbose_name
    AuthorID          = models.CharField('AuthorID(PK)',max_length=60)
    Name           = models.CharField('Name',max_length=60,blank=True)
    Age       = models.CharField('Age',max_length=10,blank=True)
    Country         = models.CharField('Country',max_length=60,blank=True)
	
class AuthorIssue(admin.ModelAdmin):
	list_display = ('AuthorID','Name','Age','Country')
	
	# def __unicode__(self):
        # return str(self.title)
		
admin.site.register(Author,AuthorIssue)