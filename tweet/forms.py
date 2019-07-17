from django.forms import ModelForm, Textarea, HiddenInput
from .models import Tweet




class TweetForm(ModelForm):
    class Meta:
        model=Tweet
        fields= ["content"]
        widgets= {"content": Textarea(attrs={'cols': 15, 'rows': 5})}



