from django import forms
from .models import *



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'author']

    #     widgets = {
    #         'image': forms.FileInput(attrs={'accept': 'image/*'})
    #     }
    #
    # def save(self, commit=True):
    #     post = super(PostForm, self).save(commit=False)
    #     if commit:
    #         post.save()
    #
    #         if 'image' in self.cleaned_data:
    #             post.image = self.cleaned_data['image']
    #             post.save()
    #     return post


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'star_given']

    def clean_star_given(self):
        star_given = self.cleaned_data.get('star_given')
        if star_given < 1 or star_given > 5:
            raise forms.ValidationError("Star rating must be between 1 and 5.")
        return star_given
