from django.shortcuts import render
from .models import Ai
from . serializers import AiSerializer 
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse 

# Create your views here.
#queryset
def ai_info(request):
    #complex Data
    ai = Ai.objects.all()
    #python dictionary
    serializer = AiSerializer(ai, many = True)
    #render json
    json_data = JSONRenderer().render(serializer.data)
    #json sent to user
    return HttpResponse(json_data, content_type = 'appliction/json')
#model instance
def ai_instamce(request,pk):
    #complex Data
    ai = Ai.objects.get(id=pk)
    #python dictionary
    serializer = AiSerializer(ai)
    #render json
    json_data = JSONRenderer().render(serializer.data)
    #json sent to user
    return HttpResponse(json_data, content_type = 'appliction/json')
    
