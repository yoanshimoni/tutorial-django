from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_items(request):
    items = [{"name": "Item1", "color": "Red"}, {"name": "Item2", "color": "Blue"}]  # Sample items
    return Response(items)
