from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, RetrieveAPIView

from accounts.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from src.app.api.serializers import UserSerializer, LikeSerializer
from app.models import Like


class MatchesListAPIView(ListAPIView):
    serializer_class = UserSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        if self.request.user.gender == "male":
            gender = "female"
        else:
            gender = "male"

        return self.model.objects.filter(gender=gender)


class MemberRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
    model = serializer_class.Meta.model
    queryset = User.objects.all()


class LikedMeListAPIView(ListAPIView):
    serializer_class = LikeSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        return self.model.objects.filter(member_id=self.request.user.id).select_related('member', )


class WhomILikedListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LikeSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        return self.model.objects.filter(user_id=self.request.user.id).select_related('user', )


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def like(request, id=None):
    member = User.objects.get(id=id)
    user = request.user
    if Like.objects.filter(member=member, user=user).exists():
        return Response({'success': 'already liked', 'status': status.HTTP_400_BAD_REQUEST})
    like = Like(member=member, user=user)
    like.save()
    return Response({'success': 'liked', 'status': status.HTTP_200_OK})


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def dislike(request, id=None):
    member = User.objects.get(id=id)
    user = request.user
    like = Like.objects.filter(member=member, user=user)
    if like:
        like.delete()
        return Response({'success': 'disliked', 'status': status.HTTP_200_OK})
    else:
        return Response({'success': 'not liked yet', 'status': status.HTTP_400_BAD_REQUEST})


class MatchesFilterListAPIView(ListAPIView):
    serializer_class = UserSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        minAge = self.request.GET['minAge']
        maxAge = self.request.GET['maxAge']
        gender = self.request.GET['gender']

        return User.objects.filter(gender=gender, age__range=[minAge, maxAge])
