from django.shortcuts import render,get_object_or_404
from blogapp.models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
def post_list_view(request):
    post_list=Post.objects.all()
    paginator = Paginator(post_list,3)
    page_number=request.GET.get('page')
    try:
        post_list = paginator.page(page_number)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'blogapp/post_list.html',{'post_list':post_list})


def post_detail_view(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,
                                status='published',
                                publish__year=year,
                                publish__month=month,
                                publish__day=day)
    return render(request,'blogapp/post_detail.html',{'post':post})
