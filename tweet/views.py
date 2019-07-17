from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from tweet.forms import TweetForm
from tweet.models import Tweet


class Homepage(View):
    def get(self,request):
        all_tweets=Tweet.objects.all()
        form=TweetForm()
        return render(request, 'tweet/Homepage.html',context={"all_tweets":all_tweets,
                                                              "form": form,})
    def post(self,request):
        form=TweetForm(request.POST)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user =request.user
            content=form.cleaned_data.get('content')
            tweet.save()
            messages.success(request, "Added")
            return redirect('homepage')
        messages.warning(request, "Error")
        return redirect("homepage")
