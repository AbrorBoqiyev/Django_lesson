from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    age = models.SmallIntegerField()

    def __str__(self):
        return self.name
    

    
class Genre(models.Model):
    name = models.CharField(max_length=100)     

    def __str__(self):
        return self.name
    
    

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.name
    
    

    
