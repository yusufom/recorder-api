# Generated by Django 3.2.13 on 2023-10-02 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_recordings_is_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='recordings',
            name='is_transcript_completed',
            field=models.BooleanField(default=False),
        ),
    ]