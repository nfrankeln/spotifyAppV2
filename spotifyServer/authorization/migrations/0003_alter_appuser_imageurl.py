# Generated by Django 4.1.4 on 2023-03-05 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0002_appuser_imageurl_appuser_spotifyid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='imageURL',
            field=models.TextField(blank=True, null=True),
        ),
    ]
