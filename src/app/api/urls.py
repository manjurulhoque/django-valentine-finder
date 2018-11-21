from django.urls import path

from src.accounts.api.views import register
from src.app.api.views import MatchesListAPIView, MemberRetrieveAPIView, LikedMeListAPIView, WhomILikedListAPIView, \
    like, dislike

urlpatterns = [
    path('matches', MatchesListAPIView.as_view()),
    path('members/<int:pk>', MemberRetrieveAPIView.as_view()),
    path('liked-me', LikedMeListAPIView.as_view()),
    path('whom-i-liked', WhomILikedListAPIView.as_view()),
    path('like/<int:id>', like),
    path('dislike/<int:id>', dislike),
]
