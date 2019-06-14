# Generated by Django 2.1.2 on 2019-06-13 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20190612_2207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item1',
            name='flag',
        ),
        migrations.RemoveField(
            model_name='item2',
            name='flag',
        ),
        migrations.AddField(
            model_name='item',
            name='flag1',
            field=models.NullBooleanField(default=None, verbose_name='入力完了フラグ1'),
        ),
        migrations.AddField(
            model_name='item',
            name='flag2',
            field=models.NullBooleanField(default=None, verbose_name='入力完了フラグ2'),
        ),
    ]
