# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, name, password, email):
        user = self.model(name=name, email=email)
        user.set_password(password)
        user.save()
        return user

    create_superuser = create_user


class User(AbstractBaseUser):
    name = models.CharField(max_length=16)
    email = models.EmailField(max_length=254, unique=True)
    mobile = models.CharField(max_length=20, blank=True)
    description = models.CharField(max_length=32, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'user'


class Item(models.Model):
    STATUS_INIT = 1
    STATUS_ON = 2
    STATUS_FINISH = 3
    STATUS_CANCEL = 4

    STATUS_CHOICES = (
        (STATUS_INIT, '未开始'),
        (STATUS_ON, '进行中'),
        (STATUS_FINISH, '已完成'),
        (STATUS_CANCEL, '已取消')
    )

    PRIORITY_LOW = 1
    PRIORITY_MIDDLE = 2
    PRIORITY_HIGH = 3

    PRIORITY_CHOICES = (
        (PRIORITY_LOW, '低'),
        (PRIORITY_MIDDLE, '中'),
        (PRIORITY_HIGH, '高')
    )

    user = models.ForeignKey(User, related_name='owner',
                             on_delete=models.CASCADE)
    content = models.TextField(null=False)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    priority = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_INIT)
    status = models.IntegerField(choices=STATUS_CHOICES, default=PRIORITY_LOW)
    finish_time = models.DateTimeField()

    def __unicode__(self):
        return (
            'user: %(username)s  content: %(content)s' %
            {'username': self.user.name, 'content': self.content}
        )

    class Meta:
        db_table = 'item'
