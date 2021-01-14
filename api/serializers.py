from rest_framework import serializers
from .models import Test, KeywordTitle, KeywordText, ScrapedUrls


class GetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test   # 要序列化的模型
        fields = '__all__'   # 要序列化的字段


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test   # 要序列化的模型
        fields = '__all__'   # 要序列化的字段


class KeywordTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeywordTitle   # 要序列化的模型
        fields = '__all__'   # 要序列化的字段


class KeywordTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeywordText   # 要序列化的模型
        fields = '__all__'   # 要序列化的字段


class ScrapedUrlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapedUrls   # 要序列化的模型
        fields = '__all__'   # 要序列化的字段