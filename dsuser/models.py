from django.db import models

# Create your models here.
class Dsuser(models.Model):
  userid = models.CharField(max_length=64,
                              verbose_name='아이디')
  useremail = models.EmailField(max_length=128,
                              verbose_name='이메일')
  password = models.CharField(max_length=64,
                              verbose_name='비밀번호')
  registered_dttm = models.DateTimeField(auto_now_add=True,
                                         verbose_name='가입일')
  
  def __str__(self):				# admin 페이지에 보여줄 문자열
			return self.userid
  
  class Meta:
    db_table = 'djangostagram_dsuser'
    verbose_name = '장고스타그램 사용자'					# 클래스명 대신 표시할 문자 
    verbose_name_plural = '장고스타그램 사용자'		# 클래스명 대신 표시할 문자(복수)