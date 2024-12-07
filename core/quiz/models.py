from django.db import models
import uuid
from django.core.exceptions import ValidationError




class MyManager(models.Manager):
    def get_available_questions(self):
        return super().get_queryset().filter(available=True)





class Question(models.Model):
    uuid     = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    question = models.CharField(max_length=1000, unique=True, help_text='be sure the question don\'n has over 1000 charachter')
    created  = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    
    objects = MyManager()
    
    
    def __str__(self) -> str:
        return str(self.question) 



class Answer(models.Model):
    uuid     = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer   = models.TextField(max_length=2000) 
    is_correct = models.BooleanField(default=False)
    created  = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return str(self.question)
    
    class Meta:
        ordering = ['-created']