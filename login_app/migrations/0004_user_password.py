# Generated by Django 2.2 on 2021-10-30 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0003_remove_user_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='password', max_length=255),
            preserve_default=False,
        ),
    ]
