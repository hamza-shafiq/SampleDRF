from rest_framework import viewsets
from .serializer import DispatchSerializer, UserSerializer
from .models import User, Dispatch

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response


class UserViewSets(viewsets.ModelViewSet):
	"""
	A simple ViewSet for listing or retrieving users.
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer


class DispatchViewSets(viewsets.ModelViewSet):
	"""
	A simple ViewSet for listing or retrieving dispatches.
	"""
	queryset = Dispatch.objects.all()
	serializer_class = DispatchSerializer

	def list(self, request):
		queryset = Dispatch.objects.all()
		serializer = DispatchSerializer(queryset, many=True)
		return Response(serializer.data)

	def retrieve(self, request, pk=None):
		queryset = Dispatch.objects.all()
		dispatch = get_object_or_404(queryset, pk=pk)
		serializer = DispatchSerializer(dispatch)
		return Response(serializer.data)
