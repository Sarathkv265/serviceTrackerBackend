from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.models import Task
from api.serializers import UserSerializer, TaskSerializer
from django.contrib.auth.models import User
from rest_framework import permissions, authentication

# Create your views here.

class UserViewSetView(ModelViewSet):

    serializer_class=UserSerializer
    queryset=User.objects.all()


class TaskViewSetView(ModelViewSet):
    
    serializer_class=TaskSerializer
    queryset=Task.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def get_queryset(self):             # to filter task based on user
        return Task.objects.filter(owner=self.request.user)