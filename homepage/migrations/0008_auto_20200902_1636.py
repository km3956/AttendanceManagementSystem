# Generated by Django 3.1 on 2020-09-02 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_auto_20200902_1633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tlogin',
            old_name='Teacher',
            new_name='TCode',
        ),
    ]
