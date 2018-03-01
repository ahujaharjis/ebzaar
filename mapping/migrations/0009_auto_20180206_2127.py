# Generated by Django 2.0.1 on 2018-02-06 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0008_auto_20180206_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryzone',
            name='pincodes',
        ),
        migrations.AddField(
            model_name='deliveryzone',
            name='pincodes',
            field=models.ManyToManyField(to='mapping.Pincode'),
        ),
    ]
