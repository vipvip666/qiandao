from django.db import models

# Create your models here.
class student_sign_in(models.Model):

    name = models.CharField(max_length=10)
    sign_time = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=20,null=True,blank=True)
    #用来检查一台电脑是否多次签名
    # cookie = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return '%s'%self.name

    class Meta:
        verbose_name = '签到表'
        verbose_name_plural = verbose_name