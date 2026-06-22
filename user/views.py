from django.shortcuts import render
from rest_framework import views, generics, permissions
from rest_framework.response import Response
# Create your views here.

class HelloView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        return Response(data={"message": "Hello world"}, status=200)