from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Blog(models.Model):
    title = models.TextField(max_length=320, null=False)
    image = models.ImageField(upload_to='images/', null=False)
    link = models.URLField(max_length=200, null=True, blank=True)
    content = RichTextUploadingField(null=False)
    LIFE_COACH = 'LIFE_COACH'
    HAND_POINTING = 'HAND_POINTING'
    EDUCATION = 'EDUCATION'
    TRANSLATE = 'TRANSLATE'
    COURSE = 'COURSE'
    CATEGORY = [
        ("LIFE_COACH", "LIFE COACH"),
        ("HAND_POINTING", "CÁCH XEM CHỈ TAY"),
        ("EDUCATION", "GIÁO DỤC TIẾNG NHẬT"),
        ("TRANSLATE", "PHIÊN DỊCH, DỊCH THUẬT NHẬT-VIỆT"),
        ("COURSE", "KHÓA HỌC"),
    ]
    category = models.CharField(
        choices=CATEGORY,
        max_length=15,
        null=False,
        default=LIFE_COACH
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)