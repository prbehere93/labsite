# Generated by Django 3.2.5 on 2021-07-28 11:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0003_alter_assignment_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='assignments', to='projects.project'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='assignments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='assignment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='projects.assignment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
