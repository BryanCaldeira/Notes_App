# Generated by Django 3.0.5 on 2020-04-27 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user_name',
            field=models.CharField(default='bryan', max_length=25),
            preserve_default=False,
        ),
    ]
