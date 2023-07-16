from django.db import models

# Create your models here.
class Department(models.Model):

    #部门表#
    title = models.CharField(verbose_name='Title', max_length=32)
    def __str__(self):
        return self.title


class UserInfo(models.Model):
    #员工表
    name = models.CharField(verbose_name='Name',max_length=16)
    password = models.CharField(verbose_name='Password',max_length=64)
    age = models.IntegerField(verbose_name='Age')
    account = models.DecimalField(verbose_name='Account Balance',max_digits=10,decimal_places=2,default=0)
    create_time = models.DateField(verbose_name='Employed Time')
    depart = models.ForeignKey(verbose_name="Department",to="department",to_field='id',on_delete=models.CASCADE)
    gender_choices = {
        (1, "女"),
        (2, "男"),
    }
    gender = models.SmallIntegerField(verbose_name='性别',choices=gender_choices)


class PrettyNum(models.Model):
    mobile = models.CharField(verbose_name='Mobile',max_length=32)
    price = models.IntegerField(verbose_name='Price',default=0)
    level_choices = (
        (1,"level 1"),
        (2,"level 2"),
        (3,"level 3"),
        (4, "level 4"),
    )
    status_choices = (
        (1,"Yes"),
        (2,"No"),
    )
    level = models.SmallIntegerField(verbose_name='Level',choices=level_choices,default=1)
    status = models.SmallIntegerField(verbose_name='Occupied',choices=status_choices,default=2)

class Admin(models.Model):
    username = models.CharField(verbose_name="adminUserName",max_length=32)
    password = models.CharField(verbose_name="password",max_length=64)

    def __str__(self):
        return self.username


class Task(models.Model):
    level_choices = (
        (1,"urgent"),
        (2,"important"),
        (3,"temporary")
    )
    level = models.SmallIntegerField(verbose_name="level", choices=level_choices, default=3)
    title = models.CharField(verbose_name="title", max_length=64)
    detail = models.TextField(verbose_name="detail")

    user = models.ForeignKey(verbose_name="person in charge",to="Admin",on_delete=models.CASCADE)

class Order(models.Model):
    Oid = models.CharField(verbose_name="order No.",max_length=64)
    title = models.CharField(verbose_name="title",max_length=32)
    price = models.IntegerField(verbose_name="price")

    status_choice=(
        (1,"unpaid"),
        (2,"paid"),
    )
    status = models.SmallIntegerField(verbose_name="status",choices=status_choice,default=1)
    admin = models.ForeignKey(verbose_name="Administrator",to="Admin", on_delete=models.CASCADE)

class Boss(models.Model):
    name = models.CharField(verbose_name='Name',max_length=32)
    age = models.IntegerField(verbose_name='Age')
    image = models.CharField(verbose_name='Avatar',max_length=128)

class City(models.Model):
    name = models.CharField(verbose_name='Name',max_length=32)
    population = models.IntegerField(verbose_name='Population')
    #本质也是CharField，但写FileField可以自动保存数据
    logo = models.FileField(verbose_name='Logo',max_length=128,upload_to='city')