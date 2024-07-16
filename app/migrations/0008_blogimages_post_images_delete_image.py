# Generated by Django 5.0.7 on 2024-07-16 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_post_amazon_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=233)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_images')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.ManyToManyField(to='app.blogimages'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
