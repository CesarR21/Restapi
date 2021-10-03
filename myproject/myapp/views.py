from django.http.response import Http404
from .models import App
from .serializers import AppSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

# Create your views here.

class AppList(APIView):

    def get(self, request):
        app = App.objects.all()
        serializer = AppSerializer(app, many=True)
        return Response (serializer.data)
    def post (self,request):
        serializer= AppSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppDeatil(APIView):

    def get_object(self,pk):
        try:
            return App.objects.get(pk=pk)
        except App.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        app = self.get_object(pk)
        serializer = AppSerializer(app)
        return Response(serializer.data)

    def put(self, request, pk):
        app = self.get_object(pk)
        serializer = AppSerializer(app, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    def delete(self, request,pk):
        app = self.get_object(pk)
        app.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

