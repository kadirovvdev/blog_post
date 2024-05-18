from pyexpat.errors import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .models import *
from django.views import View
from .forms import *

# Create your views here.

class PostListView(View):
    def get(self, request):
        post_list = Post.objects.all()
        context = {'posts': post_list}
        return render(request, 'post_list.html', context=context)


class PostDetailView(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        context = {'posts': post}
        return render(request, 'post_detail.html', context=context)




class PostCreateView(View):
    def get(self, request):
        form = PostForm()
        context = {'form': form}
        return render(request, 'post_create.html', context)

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post-list')
        context = {'form': form}
        return render(request, 'post_create.html', context)




class PostUpdateView(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(instance=post)
        return render(request, 'post_update.html', {'form': form, 'post': post})

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=post.pk)
        return render(request, 'post_update.html', {'form': form, 'post': post})



class DeletePostView(View):
    def get(self, request, pk):
        post = Post.objects.filter(pk=pk).first()
        if post:
            return render(request, 'post_delete.html', {'post': post})
        return redirect('post-list')

    def post(self, request, pk):
        post = Post.objects.filter(pk=pk).first()
        if post:
            post.delete()
        return redirect('post-list')


class AddReview(LoginRequiredMixin, View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        add_review_form = ReviewForm()
        context = {
            'post': post,
            'add_review_form': add_review_form
        }
        return render(request, 'post_review.html', context=context)

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        add_review_form = ReviewForm(request.POST)
        if add_review_form.is_valid():
            review = Review.objects.create(
                comment=add_review_form.cleaned_data['comment'],
                post=post,
                user=request.user,
                star_given=add_review_form.cleaned_data['star_given']
            )
            messages.success(request, 'Review added successfully!')
            return redirect('post-detail', pk=pk)
        context = {
            'post': post,
            'add_review_form': add_review_form
        }
        return render(request, 'post_review.html', context=context)