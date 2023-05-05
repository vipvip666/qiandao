from django.db import models

# Create your models here.

class student(models.Model):
    #这个模型用来存储导入的数据和获取导入的数据，数据每次导入之前会清空之前的数据，这样每个班级上课之前操作一次导入数据
    name = models.CharField(max_length=10)

    def __str__(self):
        return '%s'%self.name

    class Meta:
        verbose_name = '班级学生名单表'
        verbose_name_plural = verbose_name



class stu_teac(models.Model):
    boy = 1
    girl = 0
    #这个模型用来存储导入的数据和获取导入的数据，数据每次导入之前会清空之前的数据，这样每个班级上课之前操作一次导入数据
    name = models.CharField(verbose_name='学生姓名',max_length=10)
    teacher=models.CharField(verbose_name='班主任姓名',max_length=10)
    gender_choice = [
        ('男生',boy),
        ('女生',girl),
    ]
    gender = models.IntegerField(verbose_name='性别',choices=gender_choice)
    stu_id_card = models.CharField(verbose_name='证件号',max_length=20)



    def __str__(self):
        return '%s'%self.name

    class Meta:
        verbose_name = '学生信息表表单'
        verbose_name_plural = verbose_name

class excel_upload(models.Model):
    excel_name = models.CharField(verbose_name='表名',max_length=20)
    excel_file =models.FileField(verbose_name='表文件',upload_to='excel_file/',)

    def __str__(self):
        return self.excel_name

    class Meta:
        verbose_name = '学生excel表文件'
        verbose_name_plural = verbose_name