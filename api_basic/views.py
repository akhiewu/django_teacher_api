from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.serializers import Serializer
from rest_framework.utils import serializer_helpers
from .models import Teacher
from .serializers import TeacherSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


'''class TeacherAPIView(APIView):
    def get(self, request):
        Teachers = Teacher.objects.all()
        serializer = TeacherSerializer(Teachers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        Serializer= TeacherSerializer(data=request.data)
        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data, status= status.HTTP_201_CREATED)
        return Response(Serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    
    
class TeacherDetails(APIView):
        def get_object(self, id):
            try:
                return Teacher.objects.get(id=id)
            except Teacher.DoesNotExist:
                return HttpResponse(status= status.HTTP_404_NOT_FOUND)
            
        def get(self, request, id):
            teacher = self.get_object(id)
            serializer = TeacherSerializer(teacher)
            return Response(Serializer.data)        
        
    
        def post(self, request, id):
            teacher = self.get_object(id)
            serializer = TeacherSerializer(teacher)
            return Response(Serializer.data)
    
        def put(self, request, id):
            teacher = self.get_object(id)
            serializer = TeacherSerializer(teacher, data =request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
        def delete(self, request, id):
            teacher = self.get_object(id)
            teacher.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    '''
        
        
        
        
        

# Function Based API Views


 
@csrf_exempt
def teacher_list(request):
    if request.method == 'GET':
        Teachers = Teacher.objects.all()
        serializer = TeacherSerializer(Teachers, many=True)
        return JsonResponse(serializer.data, safe=False)
       # return Response(serializer.data)
    
    elif request.method =='Post':
        data = JSONParser().parse(request)
        serializer = TeacherSerializer(data=data)
       # serializer = TeacherSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
        #    return Response(serializer.data, status=status.HTTP_201_CREATED)
       # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
       
     
       #Update Part
@csrf_exempt
def teacher_detail(request,pk):
    try:
        teacher= Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return HttpResponse(dtstud=404)
    
    if request.method == 'GET':    
        serializer = TeacherSerializer(teacher)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parser(request)
        serializer = TeacherSerializer(teacher, data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.error, status=400)
    
    
    #Delete part
    
    elif request.method =='DELETE':
        teacher.delete()
        return HttpResponse(status=204)
    
    
        
     
   
   
   #Fantion Base Api View
   
   
@api_view(['GET', 'POST'])
def teacher_list(request):
    if request.method == 'GET':
        teachers = Teacher.object.all()
        Serializer = TeacherSerializer(teachers, many=True)
        return Response(Serializer.data)
    
    elif request.method == 'POST':
        Serializer = TeacherSerializer(data = request.data)
        if serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data, status= status.HTTP_201_CREATED)
        return Response(Serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
       
@api_view(['GET', 'PUT', 'DELETE'])
def teacher_detail(request, pk):
    try:
        teacher= Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return HttpResponse(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':    
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method =='DELETE':
        teacher.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    
     