from django.db import models

# Create your models here.
class Tag(models.Model):
  name = models.CharField(max_length=32, verbose_name='태그명')
  registered_dttm = models.DateTimeField(auto_now_add=True,
                                         verbose_name='작성일')
  
  def __str__(self):				# admin 페이지에 보여줄 문자열
			return self.name
  
  class Meta:
    db_table = 'djangostagram_tag'
    verbose_name = '장고스타그램 태그'					# 클래스명 대신 표시할 문자 
    verbose_name_plural = '장고스타그램 태그'		# 클래스명 대신 표시할 문자(복수)