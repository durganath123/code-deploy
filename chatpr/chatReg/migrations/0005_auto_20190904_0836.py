# Generated by Django 2.2.4 on 2019-09-04 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatReg', '0004_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='msg',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='text',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='username',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]