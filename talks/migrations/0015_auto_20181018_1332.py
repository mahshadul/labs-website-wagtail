# Generated by Django 2.0 on 2018-10-18 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0014_talklist_copy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='talk',
            old_name='exerpt',
            new_name='summary',
        ),
        migrations.AlterField(
            model_name='talk',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='talk',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
