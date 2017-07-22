from django.contrib import admin
from .models import WbImg, Wblog, Comment, CommentImg,WbUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
# 注册model使得后台可以管理
admin.site.register(WbUser, UserAdmin)
admin.site.register([WbImg, Wblog, Comment, CommentImg])
