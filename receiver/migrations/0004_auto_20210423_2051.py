# Generated by Django 3.2 on 2021-04-23 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receiver', '0003_auto_20210422_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
