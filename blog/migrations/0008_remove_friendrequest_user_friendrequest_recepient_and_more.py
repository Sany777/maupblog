# Generated by Django 5.0.3 on 2024-04-04 05:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_friendrequest'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendrequest',
            name='user',
        ),
        migrations.AddField(
            model_name='friendrequest',
            name='recepient',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='friendrequest',
            name='initiant',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='request_sender', to=settings.AUTH_USER_MODEL),
        ),
    ]