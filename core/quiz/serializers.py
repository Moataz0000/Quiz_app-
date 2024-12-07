from rest_framework import serializers
from .models import Question, Answer






class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['answer', 'is_correct', 'uuid', 'created']
    
        
    
    


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ['question', 'uuid', 'created', 'available', 'answers']
        
        


class CheckAnswerSerializer(serializers.Serializer):
    question_uuid = serializers.UUIDField()
    answer_uuid   = serializers.UUIDField()
    
    
    def validate(self, data):
        question_uuid = data['question_uuid']
        answer_uuid   = data['answer_uuid']
        
        try:
            answer = Answer.objects.get(uuid=answer_uuid, question__uuid=question_uuid)
        except Answer.DoesNotExist:
            raise serializers.ValidationError('Invalid question or answer selected.')    
        
        data['answer'] = answer
        return data