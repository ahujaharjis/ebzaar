# Generated by Django 2.0.1 on 2018-02-08 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0014_auto_20180208_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalcommrate',
            name='date_to',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='concessionalrate',
            name='date_to',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='defaultrate',
            name='date_to',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='deliveryzone',
            name='date_to',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='penalty',
            name='date_to',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='promo',
            name='date_to',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reimbursement',
            name='date_to',
            field=models.DateField(blank=True, null=True),
        ),
    ]
