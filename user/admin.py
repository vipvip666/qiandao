from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from .models import student,excel_upload,stu_teac

from django.urls import path
from django.shortcuts import render
# from django.contrib import admin

class MyView(admin.ModelAdmin):
    # def import_data_button(self, obj):
    #     url = 'https://www.baidu.com'#reverse('admin:import_data')
    #     # return format_html(f'<a href="{url}">Import Data</a>')
    #     return 1

    # import_data_button.short_description = 'Action'

    # def get_urls(self):
    #     urls = super().get_urls()
    #     my_urls = [
    #         path('my_view/', self.my_view,name='导入数据'),
    #     ]
    #     return my_urls + urls
    #
    # def my_view(self, request):
    #     return render(request, 'admin/myapp/my_view.html')
    # def export_csv(self, request, queryset):
    #     print('hhhhhh')
    #
    # def export_csv_button(self, obj):
    #     # url = reverse('admin:myapp_mymodel_export_csv') + f'?{admin.ACTION_CHECKBOX_NAME}={obj.pk}'
    #     # return format_html('<a href="{}">Export CSV</a>', url)
    #     print(666666666666)

    # export_csv_button.short_description = "Export CSV"
    # export_csv_button.allow_tags = True

    list_display = ['id','name',]
    list_display_links = ['name']
    search_fields = ['name']
    # actions = ['export_csv_button']

admin.site.register(student,MyView)


class MyteaView(admin.ModelAdmin):
    list_display = ['id', 'name','gender','stu_id_card','teacher' ]
    list_display_links = ['name']
    search_fields = ['name']

admin.site.register(stu_teac, MyteaView)




class MyteafileView(admin.ModelAdmin):
    list_display = ['id', 'excel_name','excel_file' ]
    list_display_links = ['excel_name']
    search_fields = ['excel_name']

    def save_model(self, request, obj, form, change):
        try:
            old_obj = excel_upload.objects.get(excel_name=obj.excel_name)
        except excel_upload.DoesNotExist:
            old_obj = None

        if old_obj:
            #如果浏览器上传了，则删除对应的，没有上传的不用管
            if request.FILES.get('excel_file'):
                old_obj.excel_file.delete()
                # old_obj.image1 = request.FILES['image1'] 注释掉不然有重复图片，models里面产生一个，这里产生一个
            old_obj.delete()

        super().save_model(request, obj, form, change)



admin.site.register(excel_upload, MyteafileView)