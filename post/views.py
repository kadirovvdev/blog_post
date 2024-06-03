from pyexpat.errors import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View
from .forms import *
from django import template

# Create your views here.

class PostListView(View):
    def get(self, request):
        post_list = Post.objects.all()
        context = {'posts': post_list}
        return render(request, 'post_list.html', context=context)


class PostDetailView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        review = Review.objects.filter(post=post)
        context = {'posts': post, 'review': review}
        return render(request, 'post_detail.html', context=context)




class PostCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        return render(request, 'post_create.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post-list')
        return render(request, 'post_create.html', {'form': form})




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
            star_given = add_review_form.cleaned_data.get('star_given', 0)
            if star_given and (star_given < 1 or star_given > 5):
                star_given = 0
            review = Review.objects.create(
                comment=add_review_form.cleaned_data['comment'],
                post=post,
                user=request.user,
                star_given=star_given
            )
            return redirect('post-detail', pk=pk)
        context = {
            'post': post,
            'add_review_form': add_review_form
        }
        return render(request, 'post_review.html', context=context)


class ReviewUpdate(View):
    def get(self, request, pk):
        review = Review.objects.get(pk=pk)
        form = ReviewForm(instance=review)
        if review.user != request.user:
            return HttpResponseForbidden("You cannot edit another user's review!")
        return render(request, 'review_update.html', {'form': form, 'review': review})

    def post(self, request, pk):
        review = Review.objects.get(pk=pk)
        form = ReviewForm(request.POST, instance=review)
        if review.user != request.user:
            return HttpResponseForbidden("You cannot edit another user's review!")
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=review.post.pk)
        return render(request, 'review_update.html', {'form': form, 'review': review})

class ReviewDelete(View):
    def get(self, request, pk):
        review = Review.objects.get(pk=pk)
        if review.user != request.user:
            return HttpResponseForbidden("You cannot delete another user's review!")
        return render(request, 'review_confirm_delete.html', {'review': review})

    def post(self, request, pk):
        review = Review.objects.get(pk=pk)
        if review.user != request.user:
            return HttpResponseForbidden("You cannot delete another user's review!")
        review.delete()
        return redirect('post-detail', pk=review.post.pk)






