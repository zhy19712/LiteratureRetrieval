# Generated by Django 3.1.5 on 2021-01-15 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_target'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='target',
            name='remark',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
