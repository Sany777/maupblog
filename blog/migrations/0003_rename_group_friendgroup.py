# Generated by Django 5.0.3 on 2024-04-02 17:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_user_group_owner_remove_group_date_created_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Group',
            new_name='FriendGroup',
        ),
    ]
