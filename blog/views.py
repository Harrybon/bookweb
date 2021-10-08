from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Category, Post


def index(request):
    # 首页
    post_list = Post.objects.all()   # 查询到所有的文章
    context = {'post_list': post_list }
    return render(request, 'blog/index.html', context)


def category_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    # 获取当前分类下的所有文章
    posts = category.post_set.all()
    context = {'category': category, 'post_list': posts}
    return render(request, 'blog/list.html', context)


def post_detail(request, post_id):
    # 文章详情页
    post = get_object_or_404(Post, id=post_id)
    context = {'post': post}
    return render(request, 'blog/detail.html', context)