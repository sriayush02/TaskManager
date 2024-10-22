#from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Task
from .serializers import TaskSerializer, TaskCreateSerializer

# Create Task API
class TaskCreateView(APIView):
    def post(self, request):
        serializer = TaskCreateSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            return Response(TaskSerializer(task).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Assign Task to User API
class AssignTaskView(APIView):
    def post(self, request, task_id, user_id):
        try:
            task = Task.objects.get(id=task_id)
            user = User.objects.get(id=user_id)
            task.assigned_users.add(user)
            return Response({"message": "Task assigned successfully"}, status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

# Get Tasks for Specific User API
class UserTasksView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            tasks = user.tasks.all()  # Access related tasks through the reverse relation
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)


# Create your views here.
