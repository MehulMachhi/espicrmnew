# Generated by Django 4.2.9 on 2024-07-18 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Master', '0017_campus_campus_university'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campus',
            name='campus_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='campus',
            name='campus_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='campus',
            name='campus_location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='campus',
            name='campus_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='campus',
            name='campus_phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='campus',
            name='campus_university',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Master.university'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='campus_website',
            field=models.URLField(blank=True, null=True),
        ),
    ]