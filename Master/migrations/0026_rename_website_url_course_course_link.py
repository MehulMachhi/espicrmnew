# Generated by Django 5.0.7 on 2024-08-06 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0025_alter_course_application_deadline'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='website_url',
            new_name='course_link',
        ),
    ]