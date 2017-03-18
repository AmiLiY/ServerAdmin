# -*- encoding:utf-8 -*-
# --------------------------------
# author : dbird
# create_time : 2017/3/18 16:01
# --------------------------------
import xadmin
from assets.models import Group, Asset, IDC
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = u'服务器运维管理系统'
    site_footer = u'杭州电子科技大学'
    menu_style = u'accordion'


class GroupAdmin(object):
    list_display = ['name', 'project', 'date_added', 'comment']
    search_fields = ['name', 'project', 'comment']
    list_filter = ['name', 'project', 'date_added', 'comment']


class AssetAdmin(object):
    list_display = ['intranet_ip', 'hostname', 'group', 'username', 'system_type', 'system_arch', 'status', 'env',
                    'idc', 'date_added']
    search_fields = ['intranet_ip', 'hostname', 'group', 'username', 'system_type', 'system_arch', 'status', 'env',
                     'idc']
    list_filter = ['intranet_ip', 'hostname', 'group', 'username', 'system_type', 'system_arch', 'status', 'env',
                   'idc', 'date_added']


class IDCAdmin(object):
    list_display = ['name', 'address', 'network', 'date_added', 'contact_person', 'phone']
    search_fields = ['name', 'address', 'network', 'contact_person', 'phone']
    list_filter = ['name', 'address', 'network', 'date_added', 'contact_person', 'phone']


xadmin.site.register(Group, GroupAdmin)
xadmin.site.register(Asset, AssetAdmin)
xadmin.site.register(IDC, IDCAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
