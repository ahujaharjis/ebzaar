# Generated by Django 2.0.1 on 2018-02-09 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0021_auto_20180209_0958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryzone',
            name='pincodes',
        ),
        migrations.AddField(
            model_name='deliveryzone',
            name='pincodes',
            field=models.CharField(max_length=1023, null=True),
        ),
    ]
