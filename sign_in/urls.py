from django.urls import path
from . import  views

#这里写上传文件的路由
urlpatterns = [
    path('signin/',views.sign_in ),
    path('',views.sign_in ),
    path('delete/',views.sign_delete ),
    path('unnamed/',views.unsignlist ),
    path('teacher/',views.teacher ),
]