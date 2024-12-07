from django.contrib import admin
from .models import Question, Answer



@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'uuid', 'created', 'available']
    search_fields = ['question']
    list_filter = ['available', 'created']
    
    
    



@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'is_correct', 'uuid', 'created']
    search_fields = ['question']
    list_filter = ['created', 'question', 'is_correct']   
        

  