# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-18 20:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intranet_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='\u5185\u7f51IP')),
                ('internet_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='\u5916\u7f51IP')),
                ('hostname', models.CharField(max_length=128, unique=True, verbose_name='\u4e3b\u673a\u540d')),
                ('username', models.CharField(blank=True, max_length=16, null=True, verbose_name='\u7ba1\u7406\u7528\u6237\u540d')),
                ('password', models.CharField(blank=True, max_length=256, null=True, verbose_name='\u5bc6\u7801')),
                ('mac', models.CharField(blank=True, max_length=20, null=True, verbose_name='MAC\u5730\u5740')),
                ('cpu', models.CharField(blank=True, max_length=64, null=True, verbose_name='CPU')),
                ('memory', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u5185\u5b58')),
                ('disk', models.CharField(blank=True, max_length=1024, null=True, verbose_name='\u786c\u76d8')),
                ('system_type', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u7cfb\u7edf\u7c7b\u578b')),
                ('system_version', models.CharField(blank=True, max_length=8, null=True, verbose_name='\u7cfb\u7edf\u7248\u672c\u53f7')),
                ('system_arch', models.CharField(blank=True, max_length=16, null=True, verbose_name='\u7cfb\u7edf\u5e73\u53f0')),
                ('number', models.CharField(blank=True, max_length=32, null=True, verbose_name='\u8d44\u4ea7\u7f16\u53f7')),
                ('status', models.IntegerField(blank=True, choices=[(1, '\u5df2\u4f7f\u7528'), (2, '\u672a\u4f7f\u7528'), (3, '\u62a5\u5e9f')], default=1, null=True, verbose_name='\u673a\u5668\u72b6\u6001')),
                ('asset_type', models.IntegerField(blank=True, choices=[(1, '\u7269\u7406\u673a'), (2, '\u865a\u62df\u673a'), (3, '\u4ea4\u6362\u673a'), (4, '\u8def\u7531\u5668'), (5, '\u9632\u706b\u5899'), (6, 'Docker'), (7, '\u5176\u4ed6')], null=True, verbose_name='\u4e3b\u673a\u7c7b\u578b')),
                ('env', models.CharField(blank=True, choices=[('prod', '\u751f\u4ea7\u73af\u5883'), ('test', '\u6d4b\u8bd5\u73af\u5883'), ('dev', '\u5f00\u53d1\u73af\u5883')], max_length=5, null=True, verbose_name='\u8fd0\u884c\u73af\u5883')),
                ('date_added', models.DateTimeField(auto_now=True, null=True, verbose_name='\u5f55\u5165\u65f6\u95f4')),
                ('is_active', models.BooleanField(default=True, verbose_name='\u662f\u5426\u6fc0\u6d3b')),
                ('comment', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': '\u8d44\u4ea7',
                'verbose_name_plural': '\u8d44\u4ea7',
            },
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u673a\u623f\u540d\u79f0')),
                ('contact_person', models.CharField(blank=True, default='', max_length=16, null=True, verbose_name='\u8054\u7cfb\u4eba')),
                ('phone', models.CharField(blank=True, default='', max_length=32, null=True, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('address', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='\u673a\u623f\u5730\u5740')),
                ('network', models.TextField(blank=True, default='', null=True, verbose_name='IP\u5730\u5740\u6bb5')),
                ('date_added', models.DateField(default=datetime.datetime.now, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('operator', models.CharField(blank=True, default='', max_length=32, null=True, verbose_name='\u8fd0\u8425\u5546')),
                ('comment', models.CharField(blank=True, default='', max_length=128, null=True, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'verbose_name': 'IDC\u673a\u623f',
                'verbose_name_plural': 'IDC\u673a\u623f',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True, verbose_name='\u9879\u76ee\u7ec4\u540d')),
                ('leader', models.CharField(max_length=32, verbose_name='\u9879\u76ee\u8d1f\u8d23\u4eba')),
                ('start_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u9879\u76ee\u53d1\u8d77\u65f6\u95f4')),
                ('comment', models.CharField(blank=True, max_length=160, null=True, verbose_name='\u5907\u6ce8')),
                ('time_modify', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u4fee\u6539\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u9879\u76ee\u7ec4',
                'verbose_name_plural': '\u9879\u76ee\u7ec4',
            },
        ),
        migrations.AddField(
            model_name='asset',
            name='idc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='assets.IDC', verbose_name='\u673a\u623f'),
        ),
        migrations.AddField(
            model_name='asset',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.Project', verbose_name='\u6240\u5c5e\u9879\u76ee'),
        ),
    ]
