from rest_framework import viewsets
from .models import valuationMetrics
from django.contrib.auth.models import User
from .serializers import valuationMetricsSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.parsers import JSONParser
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.response import Response
from rest_framework import status


class valuationMetricsViewSet(viewsets.ModelViewSet):
    queryset = valuationMetrics.objects.all()
    serializer_class = valuationMetricsSerializer
    http_method_names = ['get', 'head', 'put', 'patch', 'delete', 'post']

    def post(self, request, pk):
        serializer = valuationMetricsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    

    

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):

        permission_classes = []

        if self.action == 'create':
            permission_classes = [AllowAny]

        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]

        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        
        return [permission() for permission in permission_classes]
