from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post, Likes, DisLikes
from .form import CommentsForm


class PostView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/blog.html', {'post_list': posts})


class PostDitaidl(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'blog/blog_ditail.html', {'post': post})


class AddComments(View):
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class AddLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, pos_id=pk)
            return redirect(f'/{pk}')
        except:
            dislike = DisLikes.objects.get(ip=ip_client)
            dislike.delete()
            new_like = Likes()
            new_like.ip = ip_client
            new_like.pos_id = int(pk)
            new_like.save()
            return redirect(f'/{pk}')


class AddDisLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            DisLikes.objects.get(ip=ip_client, pos_id=pk)
            return redirect(f'/{pk}')
        except:
            like = Likes.objects.get(ip=ip_client)
            like.delete()
            new_dislike = DisLikes()
            new_dislike.ip = ip_client
            new_dislike.pos_id = int(pk)
            new_dislike.save()
            return redirect(f'/{pk}')