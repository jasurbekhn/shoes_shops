# Generated by Django 4.2.11 on 2024-05-23 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_article_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='video',
            field=models.CharField(default='', max_length=500, verbose_name='Video'),
        ),
    ]
