# Generated by Django 3.2.5 on 2021-07-15 09:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Assignments',
            new_name='Assignment',
        ),
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]