from django.urls import path, re_path
from . import views

app_name = 'api'   # 指定命名空间

urlpatterns = [
    path('article', views.ArticleView.as_view(), name='新增post/编辑put/获取所有get 文章'),
    path('articlefilter', views.ArticleFilterView.as_view(), name='条件查询 文章'),

]