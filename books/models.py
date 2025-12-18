from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Tytuł")
    author = models.CharField(max_length=100, verbose_name="Autor")
    publication_date = models.DateField(verbose_name="Data wydania")

    def __str__(self):
        return f"{self.title} - {self.author}"