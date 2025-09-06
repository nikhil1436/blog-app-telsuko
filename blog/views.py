from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from rest_framework import generics
from .serializers import PostSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied 
from rest_framework.pagination import PageNumberPagination
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.conf import settings 
from django.core.cache import cache
from .forms import PostForm

def blog(request):
    posts=Post.objects.select_related('author').all()
    return render(request,'homblog.html',{'posts': posts})

def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request,'post_detail.html',{'post': post})

class PostCreateView(LoginRequiredMixin, CreateView):
    model=Post
    form_class=PostForm
    template_name='post_form.html'

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    form_class=PostForm
    template_name='post_form.html'

    def test_func(self):
        post=self.get_object()
        return post.author==self.request.user

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    template_name='post_confirm_delete.html'
    success_url=reverse_lazy('blog')

    def test_func(self):
        post=self.get_object()
        return post.author==self.request.user
class StandardResultsSetPagination(PageNumberPagination):
    page_size=5
    page_size_query_param='page_size'
    max_page_size=20
class PostAPIView(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[IsAuthenticated]
    pagination_class=StandardResultsSetPagination

    @method_decorator(cache_page(60*15,key_prefix='post_list'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        cache.delete('post_list')

        

class PostApiDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[permissions.IsAuthenticated]

    def perform_update(self,serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied("you can't update this post")
        
        serializer.save()

        
    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied("you can't delete this post")
        instance.delete()
            
        
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class=CustomTokenObtainPairSerializer
    