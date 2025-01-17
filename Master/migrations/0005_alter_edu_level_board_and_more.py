# Generated by Django 4.2.9 on 2024-03-27 11:12

from django.db import migrations , models


class Migration(migrations.Migration):
    dependencies = [
        ('Master' , '0004_alter_available_services_price') ,
    ]

    operations = [
        migrations.AlterField(
            model_name='edu_level' ,
            name='Board' ,
            field=models.CharField(blank=True , max_length=100) ,
        ) ,
        migrations.AlterField(
            model_name='edu_level' ,
            name='Medium_of_Education' ,
            field=models.CharField(blank=True , max_length=100) ,
        ) ,
        migrations.AlterField(
            model_name='edu_level' ,
            name='Name_of_Institute' ,
            field=models.CharField(blank=True , max_length=100) ,
        ) ,
        migrations.AlterField(
            model_name='edu_level' ,
            name='Percentage' ,
            field=models.FloatField(blank=True) ,
        ) ,
        migrations.AlterField(
            model_name='edu_level' ,
            name='Stream' ,
            field=models.CharField(blank=True , max_length=100 , null=True) ,
        ) ,
        migrations.AlterField(
            model_name='edu_level' ,
            name='Year_of_Passing' ,
            field=models.IntegerField(blank=True) ,
        ) ,
        migrations.AlterField(
            model_name='edu_level' ,
            name='level' ,
            field=models.CharField(blank=True , max_length=100 , null=True) ,
        ) ,
    ]
