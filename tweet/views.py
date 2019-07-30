from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView

from tweet.forms import TweetForm
from tweet.models import Tweet


class Homepage(View):
    def get(self, request):
        all_tweets = Tweet.objects.all().order_by('-created')
        form = TweetForm()
        return render(request, 'tweet/Homepage.html', context={"all_tweets": all_tweets,
                                                               "form": form, })

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


class TweetUpdate(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
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