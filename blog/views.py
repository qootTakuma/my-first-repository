from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Post

# post_list.htmlを表示するが、Post内の情報を変数postsに格納してhtmlファイル上で動的に呼び出す
# この例では、今日の日付でPost内に入っているものを出された順に並び替え
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})