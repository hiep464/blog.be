# Generated by Django 4.2.16 on 2024-11-19 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_alter_blog_sub_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_sub_categories', to='myapp.subcategory'),
        ),
    ]
