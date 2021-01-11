from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.utils import json

from api.serializers import GetSerializer, PostSerializer
from api.models import Test, Proxy


class GetTest(generics.ListCreateAPIView):
    def get(self, request):
        queryset = Test.objects.all()
        response = {
            'code': 1,
            'data': [],
            'msg': 'success',
            'total': ''
        }
        serializer = GetSerializer(queryset, many=True)
        response['data'] = serializer.data
        response['total'] = len(serializer.data)
        return Response(response)


class PostTest(generics.ListCreateAPIView):
    def create(self, request):
        body = request.body
        parameter = json.loads(body)

        name = parameter['name']
        value = parameter['value']
        serializer = PostSerializer(data=parameter)
        if serializer.is_valid():
            # 调用save(), 从而调用序列化对象的create()方法,创建一条数据
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditTest(generics.RetrieveUpdateDestroyAPIView):
    def post(self, request):
        body = request.body
        parameter = json.loads(body)
        instance = Test.objects.filter(id=1).first()

        id = parameter['id']
        name = parameter['name']
        value = parameter['value']
        serializer = PostSerializer(data=parameter)
        if serializer.is_valid():
            serializer.update(instance, parameter)
        return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






