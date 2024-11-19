# Generated by Django 4.2.16 on 2024-11-19 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_blog_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Danh mục',
                'verbose_name_plural': 'Danh mục',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='page/', verbose_name='thumbnail')),
                ('url', models.URLField(max_length=500)),
                ('type', models.CharField(choices=[('HOME', 'Trang chủ'), ('DU_HOC', 'DU học'), ('DU_LICH', 'Du lịch')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='myapp.category')),
            ],
            options={
                'verbose_name': 'Danh mục con',
                'verbose_name_plural': 'Danh mục con',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='WebInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=320, verbose_name='title')),
                ('name', models.TextField(max_length=320, verbose_name='name')),
                ('slogan', models.TextField(max_length=320, verbose_name='slogan')),
                ('code', models.TextField(max_length=320, verbose_name='code')),
                ('address', models.TextField(max_length=320, verbose_name='address')),
                ('email', models.TextField(max_length=320, verbose_name='email')),
                ('website', models.TextField(max_length=320, verbose_name='website')),
                ('logo', models.ImageField(upload_to='webinfo/', verbose_name='logo')),
            ],
        ),
        migrations.CreateModel(
            name='WebInfoHotline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('DU_HOC', 'Du học'), ('DU_LICH', 'Du lịch')], max_length=20)),
                ('phone', models.TextField(max_length=320, verbose_name='phone')),
                ('web_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='web_info_hotlines', to='myapp.webinfo')),
            ],
        ),
        migrations.CreateModel(
            name='WebInfoLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('YOUTUBE', 'Trang chủ'), ('TIKTOK', 'Tiktok'), ('FACEBOOK', 'Facebook')], max_length=20)),
                ('url', models.URLField(max_length=500)),
                ('web_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='web_info_links', to='myapp.webinfo')),
            ],
        ),
        migrations.DeleteModel(
            name='LinkYoutube',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='featured',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
        migrations.AddField(
            model_name='blog',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='thumbnail'),
        ),
        migrations.AddField(
            model_name='userregister',
            name='service',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userregister',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userregister',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userregister',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_sub_categories', to='myapp.subcategory'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_categories', to='myapp.category'),
        ),
    ]
