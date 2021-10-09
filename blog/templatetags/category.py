# 在这里自定义模板标签
# https://docs.djangoproject.com/zh-hans/3.2/howto/custom-template-tags/  官方文档

from django import template
from blog.models import Category, Sidebar

register = template.Library()

@register.simple_tag
def get_category_list():
    # 全站的分类
    return Category.objects.all()

@register.simple_tag
def get_sidebar_list():
    # 全站的分类
    return Sidebar.get_sidebar()
