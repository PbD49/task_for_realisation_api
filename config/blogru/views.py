from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Blog
from .permissions import get_permissions
from .serializers import BlogSerializer


# Create your views here.
class BlogAPIView(APIView):
    # permission_classes = get_permissions

    @swagger_auto_schema(
        operation_description="Get all models",
        responses={200: BlogSerializer(many=True)}
    )
    def get(self, request):
        try:
            queryset = Blog.objects.select_related('user_id')
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response({'result': BlogSerializer(queryset, many=True).data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create a new model",
        request_body=BlogSerializer,
        responses={201: BlogSerializer()}
    )
    def post(self, request):
        try:
            serializer = BlogSerializer(data=request.data)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'result': serializer.data}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_description="Update a model",
        request_body=BlogSerializer,
        responses={200: BlogSerializer()}
    )
    def put(self, request, pk=None):
        if not pk:
            return Response({'error': 'Пожалуйста, укажите действительный ID (pk).'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            instance = Blog.objects.get(pk=pk)
        except:
            return Response({'error': 'ID не найден (pk).'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BlogSerializer(data=request.data, instance=instance)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'result': serializer.data})
        return Response(
            {'message': 'Произошла ошибка при изменении.', 'errors': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    @swagger_auto_schema(
        operation_description="Delete a model"
    )
    def delete(self, request, pk=None):
        if not pk:
            return Response({'error': 'Пожалуйста, укажите действительный ID (pk).'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            instance = Blog.objects.get(pk=pk)
        except:
            return Response({'error': 'ID (pk) не найден.'}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response({'message': 'Вы успешно удалили запись.'}, status=status.HTTP_200_OK)
