from django.urls import path, re_path
from . import views

app_name = 'api'   # 指定命名空间

urlpatterns = [
    path('gettest', views.GetTest.as_view(), name='get测试'),
    path('posttest', views.PostTest.as_view(), name='post测试'),
    path('edittest', views.EditTest.as_view(), name='edit测试'),
]