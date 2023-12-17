from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Blog(models.Model):
    title = models.TextField(_('title'), max_length=320, null=False)
    image = models.ImageField(_('image'), upload_to='images/')
    # link = models.URLField(_('link'), max_length=200, null=True, blank=True)
    featured = models.BooleanField(default=False, verbose_name='Bài viết nổi bật')
    LIFE_COACH = 'LIFE_COACH'
    HAND_POINTING = 'HAND_POINTING'
    EDUCATION = 'EDUCATION'
    TRANSLATE = 'TRANSLATE'
    COURSE = 'COURSE'
    INFO = 'INFO'
    CATEGORY = [
        ("LIFE_COACH", "LIFE COACH"),
        ("HAND_POINTING", "CÁCH XEM CHỈ TAY"),
        ("EDUCATION", "GIÁO DỤC TIẾNG NHẬT"),
        ("TRANSLATE", "PHIÊN DỊCH, DỊCH THUẬT NHẬT-VIỆT"),
        ("COURSE_LC", "KHÓA HỌC LIFE COACH"),
        ("COURSE_HP", "KHÓA HỌC CÁCH XEM CHỈ TAY"),
        ("INFO", "GIỚI THIỆU"),
    ]
    category = models.CharField(
        _('category'),
        choices=CATEGORY,
        max_length=15,
        null=False,
        default=LIFE_COACH
    )
    short_description = models.CharField(max_length=200, null=False)
    content = RichTextUploadingField(_('content'), null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)
    
class LinkYoutube(models.Model):
    title = models.TextField(_('title'), max_length=255, null=False)
    link = models.URLField(_('link'), max_length=300, null=False)
    short_description = models.CharField(max_length=300, null=True, blank=True)
    VIEWS = 'XEM NHIỀU'
    VIDEO = 'VIDEO'
    TYPE = [
        ("VIEWS", "XEM NHIỀU"),
        ("VIDEO", "VIDEO"),
    ]
    type_video = models.CharField(
        _('type_video'),
        choices=TYPE,
        max_length=15,
        null=False,
        default=VIEWS
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)

class UserRegister(models.Model):
    name = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.pk)
