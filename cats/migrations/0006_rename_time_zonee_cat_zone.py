# Generated by Django 4.1 on 2022-08-30 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0005_rename_time_zone_cat_time_zonee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cat',
            old_name='time_zonee',
            new_name='zone',
        ),
    ]
