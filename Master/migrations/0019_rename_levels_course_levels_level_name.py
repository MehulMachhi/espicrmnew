# Generated by Django 5.0.7 on 2024-07-30 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0018_alter_campus_campus_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course_levels',
            old_name='levels',
            new_name='level_name',
        ),
    ]