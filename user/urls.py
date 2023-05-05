from django.urls import path
from . import  views

#这里写上传文件的路由
urlpatterns = [
    path('upload/',views.excel_upload ),
    path('delete/',views.delete_class_excel ),
]