# Generated by Django 4.2.9 on 2024-07-02 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0015_remove_university_levels_university_levels'),
        ('Enquiry', '0016_alter_enquiry_course_interested_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='country_interested',
            field=models.ManyToManyField(to='Master.country'),
        ),
    ]
