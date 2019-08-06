from django.forms import ModelForm, Textarea

from .models import Tweet, Comments, Messages


class TweetForm(ModelForm):
    class Meta:
        model=Tweet
        fields= ["content"]
        widgets= {"content": Textarea(attrs={'cols': 15, 'rows': 5})}



class CommAddForm(ModelForm):
    class Meta:
        model= Comments
        fields = ["text_content"]
        widgets = {"text_content": Textarea(attrs={'cols': 15, 'rows': 5})}


class MessageForm(ModelForm):
    class Meta:
        model=Messages
        fields=["message"]
        widgets = {"message": Textarea(attrs={'cols': 15, 'rows': 5})}

