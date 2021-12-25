from django.core import paginator
from django.http.response import Http404, HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import redirect, render, get_object_or_404

from dsuser.models import Dsuser
from tag.models import Tag
from .models import Post
from .forms import PostForm
# Create your views here.

""" 
	홈 화면 (Post 리스트)
"""
def post_list(request):
  dsuser = None;
  
  if request.session.get('user'):
    user_id = request.session.get('user')
    dsuser = Dsuser.objects.get(pk=user_id)
  
  all_posts = Post.objects.all().order_by('-registered_dttm')		# 생성일의 역순 정렬(최근 등록 순서부터)
  page = int(request.GET.get('p', 1))														# 1페이지부터
  paginator = Paginator(all_posts, 4)														# 페이지당 출력 게시물 수 설정
  posts = paginator.get_page(page)
  
  return render(request,'post_list.html', {'posts': posts, 'dsuser': dsuser})	# 게시물 및 로그인 사용자 정보 전달

"""
	Post 입력
"""
def post_write(request):
  if not request.session.get('user'):				# 로그인이 되어 있지 않은 경우 로그인 화면으로 이동
    return redirect('/user/login/')
      
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      user_id = request.session.get('user')
      dsuser = Dsuser.objects.get(pk=user_id)
      
      tags = form.cleaned_data['tags'].split(',')				# 태그를 ',' 단위로 자름
      
      post = Post()
      post.imageurl = form.cleaned_data['imageurl']
      post.contents = form.cleaned_data['contents']
      post.writer = dsuser
      post.save()
      
      # Tag의 경우 save()를 한후 처리해야됨. - save()시 해당 객체의 id가 생성되며, 이 값을 활용하여 내부적으로 태그 저장 처리함.
      for tag in tags:
        if not tag:
          continue
        
        _tag, _ = Tag.objects.get_or_create(name=tag)		# 두번째 리턴값은 '_created'로 새로 생성된 경우 True. 추가 처리시 사용
        post.tags.add(_tag)
      
      return redirect('/')
  
  else:
    form = PostForm()
    
  return render(request,'post_write.html', {'form': form})


"""
 Post 상세보기
"""
def post_detail(request, pk):
  
  # Exception[DoesNotExist] 처리 방식
  """
  try:
    post = Post.objects.get(pk=pk)
  except Post.DoesNotExist:
    print('404')
    raise Http404('게시글을 찾을 수 없습니다.')
  """
  
  # get_object_or_404 사용 방식
  post = get_object_or_404(Post, pk=pk)
  
  return render(request,'post_detail.html', {'post': post})