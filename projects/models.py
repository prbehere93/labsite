from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import PROTECT
from django_extensions.db.models import TimeStampedModel

class Project(TimeStampedModel):
    title=models.CharField(max_length=100)
    desription=models.CharField(max_length=1000,blank=True)

    def __str__(self):
        return self.title
    

class Assignment(TimeStampedModel):
    class Status(models.TextChoices):
        COMPLETED="Completed"
        PENDING="Pending"   
        BACKLOG="Backlog"

    user=models.ForeignKey(User,on_delete=models.PROTECT,related_name='assignments') #related name can be used to reference relation of assignments with the user eg:user.assignments.add(a1,a2,a3...), user.assignments.all()
    project=models.ForeignKey(Project,on_delete=models.PROTECT, related_name='assignments') #need to verify this
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=1000,blank=True)
    status=models.CharField(max_length=20,default=Status.PENDING,choices=Status.choices)
    due_date=models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

class Comment(TimeStampedModel):
    assignment=models.ForeignKey(Assignment,on_delete=models.PROTECT,related_name='comments')
    user=models.ForeignKey(User,on_delete=models.PROTECT,related_name='comments')
    body=models.CharField(max_length=150,blank=True)            


