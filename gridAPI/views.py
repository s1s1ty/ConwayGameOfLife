# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from .models import Grid

from .serializers import GridSerializer
from .conveygame import ConveyGameLife


class GridList(generics.ListCreateAPIView):
	"""
	Retrieve, and Create a grid instance.
	"""

	queryset = Grid.objects.all()
	serializer_class  = GridSerializer

	def post(self, request):
		data = request.data
		serializer = GridSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=201)
		return Response(serializer.errors, status=400)


class GridDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Grid.objects.get(pk=pk)
        except Grid.DoesNotExist:
            raise Http404

    def get(self, request, pk):
    	grid = self.get_object(pk)
    	import pdb; pdb.set_trace()
    	if request.GET.get('after'):
    		all_age = list(request.GET.get('after'))
    		for index in all_age:
	    		obj = ConveyGameLife([[1,1,1],[0,1,0],[1,0,0]],grid.x,grid.y)
	    		re = obj.state_check()
	    		
    	
        serializer = GridSerializer(grid)
        return Response(serializer.data)





