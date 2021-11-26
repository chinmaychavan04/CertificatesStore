from django.db import models
from django.contrib.auth.models import User
from django.db.models import fields

field_list={
    ("personal","personal"),("education personal","education personal"),("certificates","certificates"),("other","other")
}

class Catagory(models.Model):
    fields=models.CharField(max_length=50)

    def __str__(self):
        return str(self.fields)

# Create your models here.
class Collection(models.Model):
    fields = models.ForeignKey(Catagory, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    files=models.FileField(upload_to='post/pdfs/')

    def __str__(self):
        return str(self.title)

        
            