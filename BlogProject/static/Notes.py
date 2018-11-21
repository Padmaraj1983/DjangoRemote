from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from blogapp.models import Post

def page_list_view(request):
    post_list=Post.objects.all()
    paginator= Paginator(post_list,3)
    page_number = request.GET.get('page')

    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list= paginator.page(1)
    except EmptyPage:
        post_list= paginator.page(paginator.num_pages)
    return render(request,'blogapp/post_list.html',{'post_list':post_list})