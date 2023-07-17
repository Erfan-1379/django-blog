# Generated by Django 4.2.3 on 2023-07-17 14:11

from django.db import migrations
import django.utils.timezone
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_managers_alter_comment_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='update',
            field=django_jalali.db.models.jDateTimeField(auto_now=True, verbose_name='تاریخ ویرایش'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=django_jalali.db.models.jDateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='update',
            field=django_jalali.db.models.jDateTimeField(auto_now=True),
        ),
    ]
