from django.db import models

class Project(models.Model):
    title=models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    image = models.FileField(upload_to='img/')

#class Comment(models.Model):
    #author=models.CharField(max_length=30)
    #body = models.TextField()
    #cteated_on = models.DateField(auto_now_add=True, db_index=True)
    #post = models.FileField(upload_to='img/')