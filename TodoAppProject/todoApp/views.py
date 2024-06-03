from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404, JsonResponse
from .models import Users, Task
from .serializers import UsersSerializer, TaskSerializers
from django.http import HttpResponse
from rest_framework.decorators import api_view

def helloWorld(request):
    return HttpResponse("Hello world")

class User(APIView):

    def get(self, request):

        all_users = Users.objects.all()

        ser = UsersSerializer(all_users, many = True)

        return Response(ser.data, status=status.HTTP_200_OK)

    # User Registration!!
    def post(self, request):

        print("request data: ", request.data)

        serializer = UsersSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            print("ser.data: ", serializer.data)
            return Response({'success': 'User Registered'}, status= status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Tasks(APIView):

    def get(self, request, pk, format = None):

        specificUser = Users.objects.get(pk = pk)

        allTasksOfUser = Task.objects.filter(TaskOfUserId = specificUser)

        serializer  = TaskSerializers(allTasksOfUser, many = True) 

        return Response(serializer.data)
    
    def post (self, request, pk):

        getUser = Users.objects.get(pk = pk)

        print("request.data: ", request.data)

        ser_tasks_create = TaskSerializers(data=request.data)      

        if ser_tasks_create.is_valid():

            ser_tasks_create.create(TaskUser = getUser, validated_data = ser_tasks_create.validated_data)

            return Response({'success': 'Task Created'},status=status.HTTP_201_CREATED)

        return Response(ser_tasks_create.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk, taskid):

        getUser = Users.objects.get(pk = pk)

        task_to_update = Task.objects.filter(TaskOfUserId = getUser).get(TaskId = taskid)

        ser = TaskSerializers(task_to_update, data=request.data, partial = True)

        if ser.is_valid():
            ser.save()

            return Response({'success': 'Task updated successfully'}, status= status.HTTP_200_OK)
        
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, taskid):

        getUser = Users.objects.get(pk = pk)

        Task.objects.filter(TaskOfUserId = getUser).get(TaskId = taskid).delete()

        return Response({'success': 'Task deleted successfully'}, status= status.HTTP_200_OK)