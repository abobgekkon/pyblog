from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator

# Create your views here.

def main(request):
    posts=Post.objects.filter(status='опубликовано')
    rubrics = Rubric.objects.all()
    paginator = Paginator(posts, 5)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {'posts':page.object_list, 'page': page, 'rubrics':rubrics}
    return render(request, 'blog/main.html', context)

def by_rubric(request, rubric_id):
    posts=Post.objects.filter(status='опубликовано').filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'posts':posts, 'rubrics':rubrics, 'current_rubric':current_rubric}
    return render(request, 'blog/by_rubric.html', context)


def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post, slug=post,
            status='опубликовано',
            publish__year=year,
            publish__month=month,
            publish__day=day)
    rubrics = Rubric.objects.all()
    context = {'post':post, 'rubrics': rubrics}

    return render(request,
            'blog/detail.html',
            context)


