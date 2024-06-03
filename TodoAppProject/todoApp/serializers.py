from rest_framework import serializers
from .models import Users, Task
from datetime import datetime

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['UserId', 'FirstName', 'LastName', 'Phone', 'Email']    
        read_only_fields = ['UserId']

    def create(self, validated_data):
        return Users.objects.create(**validated_data)

class TaskSerializers(serializers.ModelSerializer):

    class Meta:            
        model = Task
        fields = ['TaskId','TaskTitle', 'TaskDescription', 'TaskCreationTime', 'TaskStatus', 'TaskUpdatedAt', 'TaskCompletedAt'] 
        read_only_fields = ['TaskId','TaskUpdatedAt', 'TaskCompletedAt']

    def __init__(self, instance=None, data=..., **kwargs):
        super().__init__(instance, data, **kwargs)

    def create(self, TaskUser, validated_data):
        return Task.objects.create(TaskOfUserId = TaskUser, **validated_data)
    
    def update(self, instance, validated_data):

        for attr, value in validated_data.items():

            if attr == 'TaskStatus' and value == '2':
               setattr(instance, attr, value)
               instance.TaskUpdatedAt = datetime.now()

            elif attr == 'TaskStatus' and value == '3':
                
                setattr(instance, attr, value)
                instance.TaskCompletedAt = datetime.now()

            instance.save()

        return instance