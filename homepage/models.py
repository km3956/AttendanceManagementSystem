from django.db import models

class TInformation(models.Model):
    TCode = models.CharField(max_length=4)
    TFirstName = models.CharField(max_length=50)
    TMiddleName = models.CharField(max_length=50, blank = True, null = True)
    TLastName = models.CharField(max_length=50)
    TClass = models.IntegerField()
    TSection = models.CharField(max_length=3)
    def __str__(self):
        return self.TFirstName

class TLogin(models.Model):
    TCode = models.ForeignKey(TInformation, on_delete=models.CASCADE)
    TFirstName = models.CharField(max_length=50)
    TUsername = models.CharField(max_length=50)
    TPassword = models.CharField(max_length=50)
    def __str__(self):
        return self.TFirstName

