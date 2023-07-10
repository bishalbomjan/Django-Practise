import uuid
from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=200, null=True,blank=True)
    source_link = models.CharField(max_length=200,null=True,blank = True)
    #tags = models.ManyToManyField('Tags',blank=True)
    vote_total = models.IntegerField(blank=True,null=True)
    vote_ratio = models.IntegerField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)
    
    def __str__(self):
        return self.title