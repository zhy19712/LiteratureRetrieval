# Generated by Django 3.1.5 on 2021-01-15 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=255, null=True)),
                ('name', models.CharField(max_length=255)),
                ('type', models.IntegerField(max_length=1)),
                ('remark', models.CharField(max_length=255)),
            ],
        ),
    ]
