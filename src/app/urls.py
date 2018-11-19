from django.urls import path

from app.views import index, MatchesListView, MemberDetailView, like, dislike, LikedMeListView, WhomILikedListView, \
    MatchesFilterListView
from django.contrib.auth.decorators import login_required

app_name = "app"

urlpatterns = [
    path('', index),
    path('matches', login_required(MatchesListView.as_view(), login_url='/login'), name='matches'),
    path('members/<int:pk>', MemberDetailView.as_view(), name='member_detail'),
    path('like/<int:id>', like, name='like'),
    path('dislike/<int:id>', dislike, name='dislike'),
    path('liked-me', login_required(LikedMeListView.as_view(), login_url='/login'), name='liked_me'),
    path('whom-i-liked', login_required(WhomILikedListView.as_view(), login_url='/login'), name='whom_i_liked'),
    path('filter', MatchesFilterListView.as_view(), name='filter'),
]
