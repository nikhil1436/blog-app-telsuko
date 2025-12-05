from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
#JWT custom class 
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self,attrs):
        data=super().validate(attrs)
        data['user_id']=self.user.id
        data['username']=self.user.username
        data['email']=self.user.email
        return data

  
class PostSerializer(serializers.ModelSerializer):

    #getget
    author=serializers.StringRelatedField() 

    #post
    author_id=serializers.PrimaryKeyRelatedField(
    queryset= User.objects.all(),
    source='author',
    write_only=True,
    required=False 
)
     
    class Meta:
        model=Post
        fields=['id','title','content','created_at','author','author_id']
        
