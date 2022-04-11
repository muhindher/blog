from django import forms
from .models import Post, Category

#choices = [('coding', 'coding'), ('sports', 'sports'), ('entertainment', 'entertainment')]

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = fields = ('title', 'title_tag','author', 'category', 'body','read','post_pic')

        widgets ={
            'author' : forms.HiddenInput(attrs={'class':"col-md-4 mb-3", 'id': 'user'}),
        }
    

