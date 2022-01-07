from django.db.models import fields
from rest_framework import serializers
from .models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'




# class TeacherSerializer(serializers.Serializer):
#     title=serializers.CharField(max_length=100)
#     name=serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=100)
#     designation = serializers.CharField(max_length=500)
#     join_date = serializers.DateTimeField()
    
    
        
class StudentSerializer(serializers.Serializer):
    Department = serializers.CharField(max_length=100)
    Name = serializers.CharField(max_length=100)
    Roll = serializers.IntegerField()
    Semester = serializers.CharField(max_length=100)   
    
    def create(self, validated_data):
         return Teacher.objects.create(validated_data)

    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.designation = validated_data.get('designation', instance.designation)
        instance.date = validated_data.get('get', instance.date)
        instance.save()
        return instance
       
     
     
     
    def create(self, validated_data):
        return Student.objects.create(validated_data) 
     
    def update(self, instance, validated_data):
        instance.Department = validated_data.get('Department', instance.Department)
        instance.Name = validated_data.get('Name', instance.Name)
        instance.Roll = validated_data.get('Roll', instance.Roll)
        instance.Semester = validated_data.get('Semester', instance.Semester)
        instance.save()
        return instance
             
#Model Serializers







    
    
    
    
    
    