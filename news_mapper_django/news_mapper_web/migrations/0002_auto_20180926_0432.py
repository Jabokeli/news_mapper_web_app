# Generated by Django 2.1.1 on 2018-09-26 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_mapper_web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='_body',
            field=models.CharField(max_length=50000),
        ),
    ]
