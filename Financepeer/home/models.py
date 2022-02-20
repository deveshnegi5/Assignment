from django.db import models

class UserInfo(models.Model):
    userId = models.IntegerField()
    id = models.AutoField(primary_key=True)
    title= models.CharField(max_length=100)
    body= models.TextField()
    file = models.FileField(upload_to='uploads/',max_length=250,null=True,default=None)

    def __str__(self):
        return self.title
