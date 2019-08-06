"""Twitecs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from tweet.views import Homepage, TweetUpdate, TweetDelete, UserTweetListView, TweetDetailView, MessagesView, \
    MessageDetail, change_status_to_read

urlpatterns = [
    url(r"^$", Homepage.as_view(), name="homepage"),
    url(r"^update-tweet/(?P<pk>\d*)$", TweetUpdate.as_view(), name="update-tweet"),
    url(r"^delete-tweet/(?P<pk>\d*)$", TweetDelete.as_view(), name="delete-tweet"),
    url(r"^users-tweet/(?P<username>\w+)/(?P<pk>\d*)$", UserTweetListView.as_view(), name="users-tweet"),
    url(r"^detail-tweet/(?P<username>\w+)/(?P<pk>\d*)$", TweetDetailView.as_view(), name="detail-tweet"),
    url(r"^users-messages/(?P<pk>\d*)$", MessagesView.as_view(), name="users-messages"),
    url(r"^message/(?P<pk>\d*)$", MessageDetail.as_view(), name="message"),
    url(r'^ajax/change_status/(?P<pk>\d*)$', change_status_to_read, name='ajax_change_status')

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
