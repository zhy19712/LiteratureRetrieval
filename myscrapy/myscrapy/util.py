from api.models import KeywordTitle, KeywordText, ScrapedUrls, Target
from myscrapy.items import TutorialItem
from scrapy import Request
from api.serializers import KeywordTextSerializer, KeywordTitleSerializer, ScrapedUrlsSerializer, TargetSerializer

# target_type = 0 ：微信公众号
# target_type = 1 ：网站


def get_target(target_type):
    queryset = Target.objects.filter(type=target_type)
    serializer = TargetSerializer(queryset, many=True)
    return serializer.data


def get_keyword():
    title = []
    text = []
    querysetTitle = KeywordTitle.objects.all()
    serializerTitle = KeywordTitleSerializer(querysetTitle, many=True)
    for keyword in serializerTitle.data:
        title.append(keyword['keyword'])
    querysetText = KeywordText.objects.all()
    serializerText = KeywordTextSerializer(querysetText, many=True)
    for keyword in serializerText.data:
        text.append(keyword['keyword'])
    key_word = {
        'title': title,
        'text': text
    }
    return key_word


def match_keyword(content, key_word):
    for key_word_title in key_word:
        if key_word_title in content:
            return True
    return False


def not_in_scrapedUrls(url):
    queryset = ScrapedUrls.objects.filter(url=url)
    if queryset:
        return False
    return True


def add_scrapedUrls(url):
    data = {
        'url': url
    }
    serializer = ScrapedUrlsSerializer(data=data)
    if serializer.is_valid():
        # 调用save(), 从而调用序列化对象的create()方法,创建一条数据
        serializer.save()