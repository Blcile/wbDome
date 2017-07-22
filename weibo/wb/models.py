from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class WbUser(AbstractUser):
    nickname=models.CharField('用户名',max_length=20)
    password=models.CharField('密码',max_length=150)
    email=models.EmailField('邮箱')
    salt=models.CharField('salt',max_length=10)
    userImg=models.CharField(max_length=200)

    def __str__(self):
        return self.nickname

class Wblog(models.Model):
    wbuser=models.ForeignKey(WbUser,on_delete=models.CASCADE,)
    context = models.CharField('微博正文', max_length=200)
    sendtime = models.DateTimeField('发布时间')
    goods = models.IntegerField('赞')

    class Meta:
        ordering=['-sendtime']
    
    def __str__(self):
        return self.context


class Comment(models.Model):
    wbuser=models.ForeignKey(WbUser,on_delete=models.CASCADE,)
    blog = models.ForeignKey(Wblog, on_delete=models.CASCADE,)
    isImg = models.BooleanField('是否图片评论')
    context = models.CharField('评论正文', max_length=30)

    def __str__(self):
        return self.context

class WbImg(models.Model):
    blog = models.ForeignKey(Wblog, on_delete=models.CASCADE,)
    path = models.CharField('图片路径', max_length=150)
    uploadtime = models.TimeField('上传时间')

    def __str__(self):
        return self.path

class CommentImg(models.Model):
    wbuser=models.ForeignKey(WbUser,on_delete=models.CASCADE,)
    path = models.CharField('图片路径', max_length=150)
    uploadtime = models.TimeField('上传时间')

    def __str__(self):
        return self.path
