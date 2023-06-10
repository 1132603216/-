# models.py
from time import time, localtime

from django.db import models


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    sex = models.IntegerField(default=1)
    username = models.CharField(max_length=20)
    authority = models.IntegerField(default=0)
    password = models.CharField(max_length=20)
    nick = models.CharField(max_length=20)
    head = models.CharField(max_length=100, default="default.webp")

    class Meta:
        db_table = 'user'  # 设置表名


class Friend(models.Model):
    id = models.IntegerField(primary_key=True)
    userid = models.IntegerField()
    userid2 = models.IntegerField()

    class Meta:
        db_table = 'friend'  # 设置表名


# 基础病信息表
class Contents(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=10000)
    type = models.CharField(max_length=30)

    class Meta:
        db_table = 'contents'  # 设置表名


# 留言表
class Remain(models.Model):
    id = models.IntegerField(primary_key=True)
    userid = models.IntegerField()
    remain = models.CharField(max_length=5000)
    speekid = models.IntegerField()
    date = models.DateTimeField(auto_now=localtime(time()))

    class Meta:
        db_table = 'remain'  # 设置表名

# 帖子发布表
class Speak(models.Model):
    id = models.IntegerField(primary_key=True)
    userid = models.IntegerField()
    content = models.CharField(max_length=5000)
    date = models.DateTimeField(auto_now=localtime(time()))

    class Meta:
        db_table = 'speak'  # 设置表名