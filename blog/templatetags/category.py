# 在这里自定义模板标签
# https://docs.djangoproject.com/zh-hans/3.2/howto/custom-template-tags/  官方文档

from django import template
from blog.models import Category

register = template.Library()

@register.simple_tag
def get_category_list():
    return Category.objects.all()