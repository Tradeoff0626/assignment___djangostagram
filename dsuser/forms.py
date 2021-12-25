from django import forms
from django.contrib.auth.hashers import check_password

from .models import Dsuser

class LoginForm(forms.Form):
  userid = forms.CharField(
							error_messages={
								'required': '아이디를 입력해주세요.'
							},
    					max_length=64, label="아이디")
  password = forms.CharField(
    					error_messages={
								'required': '비밀번호를 입력해주세요.'
							},
         			max_length=64, widget=forms.PasswordInput, label="비밀번호")
  
  # 추가 유효성 검사
  def clean(self):
    clean_data = super().clean()		# 상속 받은 기본 clean 데이터
    userid = clean_data.get('userid')
    password = clean_data.get('password')
    
    if userid and password:
      try:
        dsuser = Dsuser.objects.get(userid=userid)
      except Dsuser.DoesNotExist:
        self.add_error('userid', '아이디가 없습니다.')
        return
        
      if not check_password(password, dsuser.password):
        self.add_error('password', '비밀번호를 틀렸습니다.')
      else:
        self.user_id = dsuser.id