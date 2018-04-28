# Generated by Django 2.0.4 on 2018-04-28 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0002_auto_20180428_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='description',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='talk',
            name='video_id',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]