from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import student_sign_in
from user.models import student
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
import openpyxl
from pathlib import Path
from django.conf import settings
#获取真实ip
# from ipware import get_client_ip
#获取班级名单


# print('班级名单：',name_list)
# print('班级人数：',len(name_list))
#改成set避免重复签到
# signed_list =set()



@csrf_exempt
def sign_in(request):
    stu_queryset = student.objects.all()
    name_list = [i.name for i in stu_queryset]
    # print(name_list)
    if request.method == 'POST':
        name = request.POST.get('sname')
        #获取客户端的ip
        # ip = request.META['REMOTE_ADDR']
        # print(ip,66666666666666666666666666666)
        # ip, is_routable = get_client_ip(request)
        # print(client_ip,is_routable)
        # print('--------------------')


        if name == 'zjf':
            return redirect('user/upload/')

        sign_queryset = student_sign_in.objects.all()
        signed_list = [i.name for i in sign_queryset]

        if name in signed_list:

            return render(request,'signin.html',{'message': f'{name}已经签到，无需重复提交'})

        if name in name_list:
            student_sign_in.objects.create(name=name)
            signed_list.append(name)
            sign_queryset = student_sign_in.objects.all()
            for i in sign_queryset:
                if i.name == name:
                    time = i.sign_time
            # print(sign_queryset)
            dic1={
                'name':name,
                'time':time,
                # 'charset': 'utf-8'
            }
            resp =  render(request,'welcome.html',dic1)
            resp.set_cookie('mycookie',name.encode('utf-8'),max_age=4500)
            return resp

        else:
            error0 = '名字写错了或者不存在,请重试'
            dicterror = {
                'error0':error0,
                # 'charset': 'utf-8'
            }
            return render(request,'signin.html',dicterror)

    return render(request,'signin.html')


def sign_delete(request):
    student_sign_in.objects.all().delete()
    try:
        # del name_list
        pass
    finally:

        return HttpResponse('删除成功')

# @never_cache
def unsignlist(request):
    #获取cookie值，也就是名字
    # mycookie_value = request.COOKIES.get('mycookie',None)
    # mycookie_value.strip('b')
    # print(mycookie_value,'-----------------------')
    # print(type(mycookie_value),'=================')
    # a = mycookie_value.decode('utf-8')
    # print(a)
    # print(type(a),'+++++++++')

    stu_queryset = student.objects.all()
    name_list = [i.name for i in stu_queryset]
    sign_queryset = student_sign_in.objects.all()
    signed_list = [i.name for i in sign_queryset]
    #显示已经签到的名单和签到的时间：
    sign_dict = {i.name:i.sign_time for i in sign_queryset}
    # ip_list = {i.name:i.ip for i in sign_queryset}
    # print(ip_list)

    unlist=[i for i in name_list if i not in signed_list]


    # 获取班级学生详细信息
    file =Path(settings.MEDIA_ROOT) / 'excel_file' / '班级学生信息.xlsx'
    # print(file)
    workbook = openpyxl.load_workbook(file)
    worksheet = workbook.active
    rows = list(worksheet.iter_rows())
    headers = [cell.value for cell in rows[1]]
    # print(headers)

    # objects = {}
    object_list = []
    # 这种方法如果重复导入会报错，id重复了。可以去掉添加id
    selected_keys = ['姓名', '班级']
    for row in rows[2:]:
        data = {headers[i]: cell.value for i, cell in enumerate(row)}
        new_data = {key:data[key] for key in selected_keys}
        object_list.append(new_data)
        # print(object_list)
        # print(new_data)

    # objects.update(object_list)

    # print(objects)



    b = len(unlist)
    dictedu={
        'un_name_list':unlist,
        'unamelen':b,
        'signdict':sign_dict,
        # 'ip_list':ip_list,
        # 'cookiename':mycookie_value,
        'data':object_list
        # 'charset': 'utf-8'

    }
    return render(request,'unsignin.html',dictedu)

def teacher(request):
    return render(request,'teacherinfo.html')