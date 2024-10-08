# Generated by Django 5.1.1 on 2024-09-16 04:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_user_following_alter_follow_follower_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='followers_count',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='following_count',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
