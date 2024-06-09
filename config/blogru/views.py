from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Blog
from .serializers import BlogSerializer


# Create your views here.
class BlogAPIView(APIView):
    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]

    def get(self, request):
        lst = Blog.objects.all()
        return Response({'answer': BlogSerializer(lst, many=True).data})

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'answer': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'Ошибка': 'Укажите id'})

        try:
            instance = Blog.objects.get(pk=pk)
        except:
            return Response({'Ошибка': 'Объект не найден'})

        serializer = BlogSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'answer': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'Ошибка': 'Укажите id'})
        instance = Blog.objects.get(pk=pk)
        instance.delete()

        return Response({"answer": "Выбранная запись была удалена " + str(pk)})
