# Generated by Django 2.1.2 on 2019-06-12 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20190612_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attribute',
            name='userid',
        ),
        migrations.AddField(
            model_name='attribute',
            name='Itemkey',
            field=models.OneToOneField(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Item'),
        ),
    ]
