# Generated by Django 4.2.9 on 2024-03-27 20:14

from django.db import migrations , models


class Migration(migrations.Migration):
    dependencies = [
        ('Master' , '0008_payment_mode_payment_status_payment_type') ,
        ('Accounts' , '0003_alter_payment_payment_date') ,
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment' ,
            name='Payment_For' ,
        ) ,
        migrations.AddField(
            model_name='payment' ,
            name='Payment_For' ,
            field=models.ManyToManyField(blank=True , to='Master.available_services') ,
        ) ,
    ]