# Generated by Django 2.0 on 2018-10-23 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0015_auto_20181018_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='video_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]