# Generated by Django 2.0.1 on 2018-02-12 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0025_auto_20180212_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reimbursement',
            name='thres_amt',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
