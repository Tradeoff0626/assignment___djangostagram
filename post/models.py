from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Post(models.Model):
  writer = models.ForeignKey('dsuser.Dsuser', on_delete=models.CASCADE,		# CASCADE - 사용자 삭제 시 해당 게시물도 삭제
                							verbose_name='작성자')
  imageurl = models.CharField(max_length=512,
                              verbose_name='이미지 주소')
  contents = models.TextField(verbose_name='내용')
  tags = models.ManyToManyField('tag.Tag', verbose_name='태그')
  registered_dttm = models.DateTimeField(auto_now_add=True,
                                         verbose_name='작성일')
  
  def __str__(self):				# admin 페이지에 보여줄 문자열
			return self.contents
  
  class Meta:
    db_table = 'djangostagram_post'
    verbose_name = '장고스타그램 게시물'					# 클래스명 대신 표시할 문자 
    verbose_name_plural = '장고스타그램 게시물'		# 클래스명 대신 표시할 문자(복수)