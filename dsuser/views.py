from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from .models import Dsuser
from .forms import LoginForm

# Create your views here.

""" 
	홈 화면
"""
def home(request):
  user_id = request.session.get('user')
  
  if user_id:
    dsuser = Dsuser.objects.get(pk=user_id)
    return HttpResponse(dsuser.userid)
  
  return HttpResponse('Home')


"""
	로그아웃 처리
"""
def logout(request):
  if request.session.get('user'):
    del(request.session['user'])
    
  return redirect('/')


"""
	로그인 처리
		- forms.py 사용
"""
def login(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      # session 정보 - is_valid()를 통해 유효한 값을 forms.py의 LoginForm.clean()으로 부터 리턴 받음.
      request.session['user'] = form.user_id
      return redirect('/')
  else:
    form = LoginForm();
  
  # print(form.errors)
  return render(request, 'login.html', {'form': form})


"""
	회원 가입 처리
"""
def register(request):
  if request.method == 'GET':
    return render(request, 'register.html')
  elif request.method == 'POST':
    userid = request.POST.get('userid', None)
    useremail = request.POST.get('useremail', None)
    password = request.POST.get('password', None)
    re_password = request.POST.get('re-password', None)
    
    res_data = {}
    if not (userid and useremail and password and re_password):
      res_data['error'] = '모든 값을 입력해야합니다.'
    elif password != re_password:
      res_data['error'] = '비밀번호가 다릅니다.'
    else:
      dsuser = Dsuser(
				userid = userid,
				useremail = useremail,
				password = make_password(password)
			)   
      dsuser.save()
      return redirect('/')
    
    return render(request, 'register.html', res_data)