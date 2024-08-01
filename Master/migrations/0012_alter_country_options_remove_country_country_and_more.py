# Generated by Django 4.2.9 on 2024-06-26 06:42

from django.db import migrations , models


class Migration(migrations.Migration):
    dependencies = [
        ('Master' , '0011_visastatus_and_more') ,
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country' ,
            options={'verbose_name': 'Country' , 'verbose_name_plural': 'Countries'} ,
        ) ,
        migrations.RemoveField(
            model_name='country' ,
            name='country' ,
        ) ,
        migrations.AddField(
            model_name='country' ,
            name='admission_process_attachment' ,
            field=models.FileField(blank=True , null=True , upload_to='admission_process/' ,
                                   verbose_name='Admission Process Attachment') ,
        ) ,
        migrations.AddField(
            model_name='country' ,
            name='admission_process_notes' ,
            field=models.TextField(blank=True , null=True , verbose_name='Admission Process Notes') ,
        ) ,
        migrations.AddField(
            model_name='country' ,
            name='admission_status' ,
            field=models.ManyToManyField(related_name='countries' , to='Master.admissionstatus' ,
                                         verbose_name='Admission Status') ,
        ) ,
        migrations.AddField(
            model_name='country' ,
            name='country_brochure' ,
            field=models.FileField(blank=True , null=True , upload_to='brochures/' , verbose_name='Country Brochure') ,
        ) ,
        migrations.AddField(
            model_name='country' ,
            name='country_name' ,
            field=models.CharField(default=1 , max_length=100 , unique=True , verbose_name='Country Name') ,
            preserve_default=False ,
        ) ,
        migrations.AddField(
            model_name='country' ,
            name='currency' ,
            field=models.CharField(default=1 , max_length=50 , verbose_name='Currency') ,
            preserve_default=False ,
        ) ,
        migrations.AddField(
            model_name='country' ,
            name='news_letter' ,
            field=models.FileField(blank=True , null=True , upload_to='news_letters/' , verbose_name='News Letter') ,
        ) ,
        migrations.AddField(
            model_name='country' ,
            name='video_attachment' ,
            field=models.FileField(blank=True , null=True , upload_to='videos/' , verbose_name='Video Attachment') ,
        ) ,
        migrations.AddField(
            model_name='country' ,
            name='visa_process_attachment' ,
            field=models.FileField(blank=True , null=True , upload_to='visa_process/' ,
                                   verbose_name='Visa Process Attachment') ,
        ) ,
        migrations.AddField(
            model_name='country' ,
            name='visa_process_notes' ,
            field=models.TextField(blank=True , null=True , verbose_name='Visa Process Notes') ,
        ) ,
        migrations.AddField(
            model_name='country' ,
            name='visa_status' ,
            field=models.ManyToManyField(related_name='countries' , to='Master.visastatus' ,
                                         verbose_name='Visa Status') ,
        ) ,
    ]
