# Generated by Django 2.1.2 on 2019-06-11 09:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0011_auto_20190611_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attribute',
            name='created_by3',
        ),
        migrations.RemoveField(
            model_name='attribute',
            name='username',
        ),
        migrations.AddField(
            model_name='attribute',
            name='user',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー'),
        ),
    ]
