from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView, CreateView, ListView, DetailView

from tweet.forms import TweetForm
from tweet.models import Tweet, Comments
from users.models import MyUser


class Homepage(View):
    def get(self, request):
        all_tweets = Tweet.objects.all().order_by('-created')
        all_comments = Comments.objects.all().order_by('-created_comment')
        form = TweetForm()
        return render(request, 'tweet/Homepage.html', context={"all_tweets": all_tweets,
                                                               "form": form,
                                                               "all_comments": all_comments})

    def post(self, request):
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            messages.success(request, "Added")
            return redirect('homepage')
        messages.warning(request, "Error")
        return redirect("homepage")


class TweetUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Tweet
    fields = ["content"]
    success_url = reverse_lazy("homepage")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user


class TweetDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Tweet
    success_url = reverse_lazy('homepage')

    def test_func(self):
        return self.request.user == self.get_object().user


class CommentCreate(CreateView):
    model = Comments


class UserTweetListView(ListView):
    model = Tweet
    context_object_name = "tweets"
    template_name = 'tweet/list_tweet_user.html'

    def get_queryset(self):
        user = get_object_or_404(MyUser, username=self.kwargs.get('username'))
        return Tweet.objects.filter(user=user)

class TweetDetailView(DetailView):
    model=Tweet
    template_name = 'tweet/tweet_detail.html'

    def get_context_data(self, **kwargs):
        print(self.object.id)
        context = super().get_context_data(**kwargs)
        context['tweet'] = Tweet.objects.get(id=self.object.id)
        return context

