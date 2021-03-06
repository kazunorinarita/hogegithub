# Generated by Django 2.1.2 on 2019-06-11 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20190609_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, default='', editable=False, max_length=150, null=True)),
                ('full_name', models.CharField(blank=True, default='', editable=False, max_length=100, null=True)),
                ('department', models.CharField(blank=True, default='', editable=False, max_length=100, null=True)),
                ('job_type', models.CharField(blank=True, default='', editable=False, max_length=100, null=True)),
                ('title', models.CharField(blank=True, default='', editable=False, max_length=100, null=True)),
            ],
        ),
    ]
