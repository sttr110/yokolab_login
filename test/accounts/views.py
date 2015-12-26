from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

from accounts.forms import UserForm
from django.contrib.auth.models import User


def create_user(request):
  #POSTのとき
  if request.method == 'POST':
    user = User()
    form = UserForm(request.POST, instance=user)
    user = form.save(commit=False)

    User.objects.create_user(user.username, 'lennon@thebeatles.com', user.password)
    return HttpResponse("Created " + user.username)

  #GETのとき
  user = User()
  form = UserForm(instance=user)

  return render_to_response('accounts/create_user.html',
                            dict(form=form),
                            context_instance=RequestContext(request))
  


@login_required
def user_profile(request):
    context = RequestContext(request,
                             {'user': request.user})
    return render_to_response('accounts/user_profile.html',
                              context_instance=context)

#ログインした状態じゃないとtestが呼ばれない
@login_required
def test(request):
  return HttpResponse("hello world")
 
