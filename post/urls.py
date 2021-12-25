from django.urls import path
from . import views

urlpatterns = [
		# path('', views.post_list),							# 바로 연결로 인한 미사용
    # path('upload/', views.post_write),			# 바로 연결로 인한 미사용
    path('<int:pk>/', views.post_detail)
]