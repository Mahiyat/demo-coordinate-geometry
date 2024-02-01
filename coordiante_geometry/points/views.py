from django.shortcuts import render
from django.core.serializers import serialize
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import json

from .models import Point
from .serializers import PointSerializer

# Create your views here.
@api_view(['GET'])
def average(request):
  p=Point.objects.all()
  serializer = PointSerializer(p, context={'request': request}, many=True)
  n=0
  sx=0
  sy=0
  for point in serializer.data:
    sx+=point['x']
    sy+=point['y']
    n+=1
  if n==0:
    avgx=0
    avgy=0
  else:
    avgx=round(sx/n)
    avgy=round(sy/n)
  return Response({'avg': {'x': avgx, 'y': avgy}}, status=status.HTTP_200_OK)
@api_view(['PUT'])
def upsert(request):
  d=request.data
  try:
    point=Point.objects.get(x=d['x'], y=d['y'])
  except Point.DoesNotExist:
    serializer=PointSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      tmp=serializer.data
      return Response(status=status.HTTP_201_CREATED, data={'added': {'x': tmp['x'], 'y': tmp['y']}})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  return Response(data={'x': d['x'], 'y': d['y']},status=status.HTTP_200_OK)