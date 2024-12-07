from django.shortcuts import get_object_or_404
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer, CheckAnswerSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.views import APIView




class QuestionListView(viewsets.ViewSet):
    """
    CRUD of availabe questions.
    """
    def list(self, request):
        queryset = Question.objects.get_available_questions().prefetch_related('answers')
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        queryset = get_object_or_404(Question, pk=pk, available=True)
        serializer = QuestionSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        data = request.data 
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'Object Created Successfully.'},
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )  
        
    def update(self, request, pk=None):
        object = get_object_or_404(Question, pk=pk, available=True)
        new_data = request.data
        partial = request.method == 'PATCH'
        serializer = QuestionSerializer(object, data=new_data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'Object Modifidy Successfully.'},
                status=status.HTTP_200_OK
            )
        return Response(
            {serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )          
        
    def destroy(self, request, pk=None):
        object = get_object_or_404(Question, pk=pk, available=True)    
        object.delete()
        return Response(
            {'message': 'object deleted successfully.'},
            status=status.HTTP_204_NO_CONTENT
        )
        
        
        
        


class CheckAnswerView(APIView):
    """
    check if the user's selected answer is correct.
    """

    def post(self, request):
        data = request.data
        serializer = CheckAnswerSerializer(data=data)
        if serializer.is_valid():
            answer = serializer.validated_data['answer']
            is_correct = answer.is_correct
            return Response(
                {
                "message": "Answer check}ed successfully.",
                "is_correct": is_correct
                },
                status=status.HTTP_200_OK
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    