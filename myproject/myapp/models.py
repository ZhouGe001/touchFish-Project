from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255,verbose_name='姓名')
    age = models.SmallIntegerField(null=True,verbose_name='年龄')
    email = models.EmailField(unique=True,verbose_name='邮箱')
    password = models.CharField(max_length=255,verbose_name='密码')
    address = models.CharField(max_length=255,verbose_name='地址')
    phone = models.CharField(max_length=255,verbose_name='手机号')
    choice=(
        (1,'Male'),
        (0,'Female')
    )
    gender = models.CharField(max_length=255,choices=choice,verbose_name='性别')
    role = models.CharField(max_length=255,verbose_name='角色')
    status = models.CharField(max_length=255,verbose_name='状态')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    last_online_at = models.DateTimeField(auto_now=True,verbose_name='最后登录时间')