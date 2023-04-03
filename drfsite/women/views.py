from rest_framework import generics, viewsets
from .models import Women, Category
from .serializer import WomenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms.models import model_to_dict
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework import viewsets

viewsets.ModelViewSet

class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly,)