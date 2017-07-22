from django.db import models

# Create your models here.


class Wblog(models.Model):
    context = models.CharField('微博正文', max_length=200)
    sendtime = models.DateTimeField('发布时间')
    goods = models.IntegerField('赞')

    class Meta:
        ordering=['-sendtime']
    
    def __str__(self):
        return self.context


class Comment(models.Model):
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
    path = models.CharField('图片路径', max_length=150)
    uploadtime = models.TimeField('上传时间')

    def __str__(self):
        return self.path
