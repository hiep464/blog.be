from .models import Blog, UserRegister, WebInfo, Page, WebInfoLink, WebInfoHotline
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegister
        fields = '__all__'

class WebInfoLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebInfoLink
        fields = '__all__'

class WebInfoHotlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebInfoHotline
        fields = '__all__'

class WebInfoSerializer(serializers.ModelSerializer):
    web_info_links = WebInfoLinkSerializer(many=True)
    web_info_hotlines = WebInfoHotlineSerializer(many=True)

    class Meta:
        model = WebInfo
        fields = ['id', 'title', 'name', 'slogan', 'code', 'address', 'email', 'website', 'logo', 'web_info_links', 'web_info_hotlines']
    
class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'
