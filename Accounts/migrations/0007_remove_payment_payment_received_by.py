# Generated by Django 4.2.9 on 2024-03-27 20:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('Accounts' , '0006_alter_payment_payment_received_by') ,
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment' ,
            name='payment_received_by' ,
        ) ,
    ]