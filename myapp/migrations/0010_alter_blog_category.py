# Generated by Django 4.2.7 on 2023-12-21 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_linkyoutube_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('LIFE_COACH', 'LIFE COACH'), ('FUNCTIONAL_FOODS', 'THỰC PHẨM CHỨC NĂNG'), ('EDUCATION', 'GIÁO DỤC TIẾNG NHẬT'), ('TRANSLATE', 'PHIÊN DỊCH, DỊCH THUẬT NHẬT-VIỆT'), ('COURSE_LC', 'KHÓA HỌC LIFE COACH'), ('COURSE_HP', 'KHÓA HỌC CÁCH XEM CHỈ TAY'), ('COURSE_JP', 'KHÓA HỌC TIẾNG NHẬT'), ('INFO', 'GIỚI THIỆU')], default='LIFE_COACH', max_length=20, verbose_name='category'),
        ),
    ]