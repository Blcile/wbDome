from django.db import models

# Create your models here.


class wblog(models.Model):
    context = models.CharField('微博正文', max_length=200)
    time = models.DateTimeField('发布时间')
    goods = models.IntegerField('赞')


class comment(models.Model):
    blog = models.ForeignKey(wblog, on_delete=models.CASCADE,)
    isImg = models.BooleanField('是否图片评论')
    context = models.CharField('评论正文', max_length=30)


class wbImg(models.Model):
    blog = models.ForeignKey(wblog, on_delete=models.CASCADE,)
    path = models.CharField('图片路径', max_length=150)
    uploadtime = models.TimeField('上传时间')

class commentImg(models.Model):
    path = models.CharField('图片路径', max_length=150)
    uploadtime = models.TimeField('上传时间')
