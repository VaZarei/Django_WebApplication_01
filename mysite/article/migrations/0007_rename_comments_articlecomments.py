# Generated by Django 5.0.6 on 2024-05-19 14:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_remove_articlemodel_slug_comments_articlemodel_slug'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='ArticleComments',
        ),
    ]
