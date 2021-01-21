from rest_framework import serializers
from .models import KeywordTitle, KeywordText, ScrapedUrls, Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article  # 要序列化的模型
        fields = '__all__'  # 要序列化的字段

        def create(self, validated_data):
            url = validated_data['url']
            title = validated_data['title']
            time = validated_data['time']
            text = validated_data['text']
            article = Article.objects.create(
                url=url,
                title=title,
                time=time,
                text=text
            )
            return article

        def update(self, instance, validated_data):
            url = validated_data['url']
            title = validated_data['title']
            time = validated_data['time']
            text = validated_data['text']

            instance.title = title
            instance.url = url
            instance.time = time
            instance.text = text
            instance.save()
            return instance


class KeywordTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeywordTitle  # 要序列化的模型
        fields = '__all__'  # 要序列化的字段


class KeywordTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeywordText  # 要序列化的模型
        fields = '__all__'  # 要序列化的字段


class ScrapedUrlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapedUrls  # 要序列化的模型
        fields = '__all__'  # 要序列化的字段
