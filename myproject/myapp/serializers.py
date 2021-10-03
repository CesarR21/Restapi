from django.db.models import fields
from rest_framework import serializers
from .models import App

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App 
        fields = [ 'id','title','artist','album','release_date']
        