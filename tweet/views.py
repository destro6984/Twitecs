from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import UpdateView, DeleteView, ListView, DetailView
from django.views.generic.edit import FormMixin

from tweet.forms import TweetForm, CommAddForm, MessageForm
from tweet.models import Tweet, Comments, Messages
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



class UserTweetListView(FormMixin,LoginRequiredMixin,ListView):
    model = Tweet
    context_object_name = "tweets"
    template_name = 'tweet/list_tweet_user.html'
    form_class = MessageForm

    def get_success_url(self):
        return reverse('users-tweet', kwargs={'username': self.kwargs.get('username'),"pk":self.kwargs.get('pk')})

    def get_queryset(self):
        user = get_object_or_404(MyUser, username=self.kwargs.get('username'))
        return Tweet.objects.filter(user=user)
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form_send_message = form.save(commit=False)
            form_send_message.from_user_id = request.user.id
            form_send_message.to_user_id = self.kwargs.get('pk')
            form_send_message.save()
            messages.success(request, "Send")
            return self.form_valid(form)
        else:
            messages.success(request, "Error")
            return self.form_invalid(form)

class TweetDetailView(FormMixin, LoginRequiredMixin, DetailView):
    model = Tweet
    template_name = 'tweet/tweet_detail.html'
    form_class = CommAddForm

    def get_success_url(self):
        return reverse('detail-tweet', kwargs={'username': self.object.user,
                                               'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            form_add_com = form.save(commit=False)
            form_add_com.tweet_id = self.get_object().id
            form_add_com.author_id = request.user.id

            form_add_com.save()
            messages.success(request, "Commented")
            return self.form_valid(form)
        else:
            messages.success(request, "Error")
            return self.form_invalid(form)

    def form_valid(self, form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comments.objects.filter(tweet_id=self.object.id).order_by('-created_comment')
        return context


class MessagesView(LoginRequiredMixin,UserPassesTestMixin,ListView):
    model= Messages
    field='__all__'
    template_name = "tweet/list_messages.html"

    def get_queryset(self):
        user = get_object_or_404(MyUser, id=self.kwargs.get('pk'))
        return Messages.objects.filter(to_user=user).order_by('-send_time')
    def test_func(self):
        user = get_object_or_404(MyUser, id=self.kwargs.get('pk'))
        return self.request.user == user


class MessageDetail(View):
    def get(self,request,pk):
        mess=Messages.objects.get(id=pk)
        return render(request,'tweet/message_detail.html',context={"mess":mess})


def change_status_to_read(request,pk):
    pk= request.GET.get("pk")
    is_read = json.loads(request.GET.get('is_read', False))
    message_to_change = Messages.objects.get(id=pk)
    try:
        message_to_change.is_read = is_read
        message_to_change.save()
        return JsonResponse({"success": True})
    except Exception as e:
        return JsonResponse({"success": False})
