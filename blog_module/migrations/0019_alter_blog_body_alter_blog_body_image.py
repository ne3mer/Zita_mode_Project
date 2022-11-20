# Generated by Django 4.1.3 on 2022-11-20 10:25

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_module', '0018_alter_blog_body_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=ckeditor.fields.RichTextField(default=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='body_image',
            field=models.ImageField(default='', upload_to='images/blog/%Y/%m/%d', verbose_name='تصویر بدنه آموزش'),
        ),
    ]
