# Generated by Django 3.1 on 2020-09-01 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_tinformation_tlogin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tinformation',
            name='TMiddleName',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
