from django.contrib import admin
from .models import WbImg, Wblog, Comment, CommentImg

# Register your models here.
# 注册model使得后台可以管理
admin.site.register([WbImg, Wblog, Comment, CommentImg])
