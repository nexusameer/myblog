# Generated by Django 5.0.7 on 2024-07-17 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_blogimages_post_images_delete_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='post_videos/'),
        ),
    ]
