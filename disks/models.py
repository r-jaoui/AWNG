from django.db import models


# Create your models here.
class Album(models.Model):
    Title = models.CharField(max_length=160)
    Artist = models.ForeignKey("Artist", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "album"
        ordering = ['Title']

    def __str__(self):
        return self.Title


class Artist(models.Model):
    Name = models.CharField(max_length=120)

    class Meta:
        verbose_name = "artist"

    def __str__(self):
        return self.Name


class Track(models.Model):
    Name = models.CharField(max_length=200)
    Album = models.ForeignKey("Album", on_delete=models.CASCADE)
    Composer = models.CharField(max_length=220)
    Milliseconds = models.TextField()
    Bytes = models.IntegerField()
    UnitPrice = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "track"
        ordering = ['Name', 'Album', 'Milliseconds', 'UnitPrice', 'Composer', 'Bytes']

    def __str__(self):
        return self.Name
