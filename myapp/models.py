from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    # description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Danh mục'
        verbose_name_plural = 'Danh mục'
        ordering = ['name']

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    # description = models.TextField(blank=True, null=True)

    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.CASCADE, related_name='sub_categories'
    )

    class Meta:
        verbose_name = 'Danh mục con'
        verbose_name_plural = 'Danh mục con'
        ordering = ['name']

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(_('title'), max_length=200, null=False)
    short_description = models.TextField(_('short_description'), max_length=320, null=True, blank=True)
    
    thumbnail = models.ImageField(_('thumbnail'), upload_to='blog/', null=True, blank=True)

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='blog_categories'
    )

    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, related_name='blog_sub_categories', null=True, blank=True
    ) 

    content = RichTextUploadingField(_('content'), null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)

class Page(models.Model):
    HOME = 'HOME'
    DU_HOC = 'DU_HOC'
    DU_LICH = 'DU_LICH'

    PAGES_CHOICES = [
        (HOME, 'Trang chủ'),
        (DU_HOC, 'Du học'),
        (DU_LICH, 'Du lịch'),
    ]

    thumbnail = models.ImageField(_('thumbnail'), upload_to='page/', null=False, blank=False)
    url = models.URLField(max_length=500, null=False, blank=False)

    type = models.CharField(
        max_length=20,
        choices=PAGES_CHOICES,
        null=False,
        blank=False
    )


class WebInfo(models.Model):
    title = models.CharField(_('title'), max_length=320, null=False)
    name = models.CharField(_('name'), max_length=320, null=False)
    slogan = models.CharField(_('slogan'), max_length=320, null=False)
    code = models.CharField(_('code'), max_length=320, null=False)
    address = models.CharField(_('address'), max_length=320, null=False)
    email = models.CharField(_('email'), max_length=320, null=False)
    website = models.CharField(_('website'), max_length=320, null=False)
    logo = models.ImageField(_('logo'), upload_to='webinfo/', null=False, blank=False)

class WebInfoLink(models.Model):
    web_info = models.ForeignKey(
        WebInfo, on_delete=models.CASCADE, related_name='web_info_links'
    )

    YOUTUBE = 'YOUTUBE'
    TIKTOK = 'TIKTOK'
    FACEBOOK = 'FACEBOOK'

    TYPE_CHOICES = [
        (YOUTUBE, 'Youtube'),
        (TIKTOK, 'Tiktok'),
        (FACEBOOK, 'Facebook'),
    ]

    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        null=False,
        blank=False
    )

    url = models.URLField(max_length=500, null=False, blank=False)

class WebInfoHotline(models.Model):
    web_info = models.ForeignKey(
        WebInfo, on_delete=models.CASCADE, related_name='web_info_hotlines'
    )

    DU_HOC = 'DU_HOC'
    DU_LICH = 'DU_LICH'

    TYPE_CHOICES = [
        (DU_HOC, 'Du học'),
        (DU_LICH, 'Du lịch'),
    ]

    type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
        null=False,
        blank=False
    )

    phone = models.CharField(_('phone'), max_length=320, null=False)

class UserRegister(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    service = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.pk)
