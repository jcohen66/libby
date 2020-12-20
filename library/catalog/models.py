from django.db import models


# Create your models here.
class Book(models.Model):
    """Model definition for MODELNAME."""

    # TODO: Define fields here

    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description")

    class Meta:
        """Meta definition for MODELNAME."""
        ordering = ['-id']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        """Unicode representation of Book."""
        return self.title

class Author(models.Model):
    """Model definition for Author."""

    # TODO: Define fields here
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)

    class Meta:
        """Meta definition for Author."""
        ordering = ['last_name', 'first_name']
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        """Unicode representation of Author."""
        return f'{self.last_name}, {self.first_name}'

