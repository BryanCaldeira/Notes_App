# Generated by Django 3.0.5 on 2020-04-28 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0002_post_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='')),
            ],
        ),
    ]