# Generated by Django 4.1.4 on 2023-03-10 20:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotifyapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='spotifytoken',
            name='access_token_expiration',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 10, 20, 59, 21, 776175, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
