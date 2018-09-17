# Generated by Django 2.0 on 2018-08-22 20:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0007_auto_20180816_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Talk date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='talk',
            name='location',
            field=models.CharField(default='WaKeeney, Kansas', max_length=100),
            preserve_default=False,
        ),
    ]
