from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from accounts.models import User
from app.models import Like


def index(request):
    return render(request, 'home.html', {})


# @login_required(login_url='/login')
# def matches(request):
#     if request.user.gender == "male":
#         gender = "female"
#     else:
#         gender = "male"
#
#     users = User.objects.filter(gender=gender)
#     return render(request, 'matches.html', {
#         'matches': users
#     })


class MatchesListView(ListView):
    model = User
    context_object_name = "matches"
    template_name = 'matches.html'
    paginate_by = 8

    def get_queryset(self):
        if self.request.user.gender == "male":
            gender = "female"
        else:
            gender = "male"

        return User.objects.filter(gender=gender)


class MemberDetailView(DetailView):
    model = User
    context_object_name = "user"
    template_name = "memberdetail.html"


class LikedMeListView(ListView):
    model = Like
    context_object_name = "likes"
    template_name = "likedme.html"

    def get_queryset(self):
        return Like.objects.filter(member_id=self.request.user.id)


class WhomILikedListView(ListView):
    model = Like
    context_object_name = "likes"
    template_name = "whomiliked.html"
    paginate_by = 4

    def get_queryset(self):
        return Like.objects.filter(user_id=self.request.user.id)


@login_required(login_url='/login')
def like(request, id=None):
    member = User.objects.get(id=id)
    user = request.user
    like = Like(member=member, user=user)
    like.save()
    return redirect('/matches')


@login_required(login_url='/login')
def dislike(request, id=None):
    member = User.objects.get(id=id)
    user = request.user
    like = Like.objects.filter(member=member, user=user)
    if like:
        like.delete()
    return redirect('/matches')


# @login_required(login_url='/login')
# def liked_me(request):
#     likes = Like.objects.filter(member_id=request.user.id)
#     return render(request, "likedme.html", {
#         'likes': likes
#     })

class MatchesFilterListView(ListView):
    model = User
    context_object_name = "matches"
    template_name = 'filtermatches.html'
    paginate_by = 8

    def get_queryset(self):
        minAge = self.request.GET['minAge']
        maxAge = self.request.GET['maxAge']
        gender = self.request.GET['gender']

        return User.objects.filter(gender=gender, age__range=[minAge, maxAge])
