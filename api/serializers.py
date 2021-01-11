from rest_framework import serializers
from .models import Test


class GetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test   # 要序列化的模型
        fields = '__all__'   # 要序列化的字段


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test   # 要序列化的模型
        fields = '__all__'   # 要序列化的字段