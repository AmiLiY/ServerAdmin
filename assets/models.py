# _*_ coding:utf-8 _*_

from __future__ import unicode_literals

from django.db import models

# Create your models here.
ASSET_ENV = (
    (1, u'生产环境'),
    (2, u'测试环境')
)

ASSET_STATUS = (
    (1, u"已使用"),
    (2, u"未使用"),
    (3, u"报废")
)

ASSET_TYPE = (
    (1, u"物理机"),
    (2, u"虚拟机"),
    (3, u"交换机"),
    (4, u"路由器"),
    (5, u"防火墙"),
    (6, u"Docker"),
    (7, u"其他")
)

GROUP_TYPE = (
    ('P', 'PRIVATE'),
    ('A', 'ASSET'),
)


class Group(models.Model):
    name = models.CharField(max_length=80, unique=True, verbose_name=u'组名')
    project = models.CharField(max_length=80, blank=True, null=True, verbose_name=u'项目名')
    comment = models.CharField(max_length=160, blank=True, null=True, verbose_name='备注')
    date_added = models.DateField(auto_now=True, null=True, verbose_name=u'添加时间')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'资产组'
        verbose_name_plural = verbose_name


class IDC(models.Model):
    name = models.CharField(max_length=32, verbose_name=u'机房名称')
    contact_person = models.CharField(max_length=16, blank=True, null=True, default='', verbose_name=u'联系人')
    phone = models.CharField(max_length=32, blank=True, null=True, default='', verbose_name=u'联系电话')
    address = models.CharField(max_length=128, blank=True, null=True, default='', verbose_name=u"机房地址")
    network = models.TextField(blank=True, null=True, default='', verbose_name=u"IP地址段")
    date_added = models.DateField(auto_now=True, null=True, verbose_name=u'创建时间')
    operator = models.CharField(max_length=32, blank=True, default='', null=True, verbose_name=u"运营商")
    comment = models.CharField(max_length=128, blank=True, default='', null=True, verbose_name=u"备注")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"IDC机房"
        verbose_name_plural = verbose_name


class Asset(models.Model):
    intranet_ip = models.GenericIPAddressField(blank=True, null=True, verbose_name=u"内网IP")
    internet_ip = models.GenericIPAddressField(max_length=255, blank=True, null=True, verbose_name=u"外网IP")
    hostname = models.CharField(unique=True, max_length=128, verbose_name=u"主机名")
    group = models.ForeignKey(Group, blank=True, verbose_name=u"所属主机组")
    username = models.CharField(max_length=16, blank=True, null=True, verbose_name=u"管理用户名")
    password = models.CharField(max_length=256, blank=True, null=True, verbose_name=u"密码")
    idc = models.ForeignKey(IDC, blank=True, null=True, on_delete=models.SET_NULL, verbose_name=u'机房')
    mac = models.CharField(max_length=20, blank=True, null=True, verbose_name=u"MAC地址")
    cpu = models.CharField(max_length=64, blank=True, null=True, verbose_name=u'CPU')
    memory = models.CharField(max_length=128, blank=True, null=True, verbose_name=u'内存')
    disk = models.CharField(max_length=1024, blank=True, null=True, verbose_name=u'硬盘')
    system_type = models.CharField(max_length=32, blank=True, null=True, verbose_name=u"系统类型")
    system_version = models.CharField(max_length=8, blank=True, null=True, verbose_name=u"系统版本号")
    system_arch = models.CharField(max_length=16, blank=True, null=True, verbose_name=u"系统平台")
    number = models.CharField(max_length=32, blank=True, null=True, verbose_name=u'资产编号')
    status = models.IntegerField(choices=ASSET_STATUS, blank=True, null=True, default=1, verbose_name=u"机器状态")
    asset_type = models.IntegerField(choices=ASSET_TYPE, blank=True, null=True, verbose_name=u"主机类型")
    env = models.IntegerField(choices=ASSET_ENV, blank=True, null=True, verbose_name=u"运行环境")
    date_added = models.DateTimeField(auto_now=True, null=True, verbose_name=u'录入时间')
    is_active = models.BooleanField(default=True, verbose_name=u"是否激活")
    comment = models.CharField(max_length=128, blank=True, null=True, verbose_name=u"备注")

    def __unicode__(self):
        return self.internet_ip + '-' + self.hostname

    class Meta:
        verbose_name = u'资产'
        verbose_name_plural = verbose_name
