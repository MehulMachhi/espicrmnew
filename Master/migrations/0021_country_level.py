# Generated by Django 5.0.7 on 2024-08-01 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0020_rename_levels_university_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='level',
            field=models.ManyToManyField(blank=True, null=True, to='Master.course_levels'),
        ),
    ]
