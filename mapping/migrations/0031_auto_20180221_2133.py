# Generated by Django 2.0.1 on 2018-02-21 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0030_auto_20180214_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='additionalcommrate',
            name='store_name',
        ),
        migrations.RemoveField(
            model_name='concessionalrate',
            name='category',
        ),
        migrations.RemoveField(
            model_name='concessionalrate',
            name='sku',
        ),
        migrations.RemoveField(
            model_name='concessionalrate',
            name='store_name',
        ),
        migrations.RemoveField(
            model_name='defaultrate',
            name='store_name',
        ),
        migrations.RemoveField(
            model_name='deliveryzone',
            name='store_name',
        ),
        migrations.RemoveField(
            model_name='penalty',
            name='store_name',
        ),
        migrations.RemoveField(
            model_name='penalty_orders',
            name='store_name',
        ),
        migrations.RemoveField(
            model_name='promo',
            name='sku',
        ),
        migrations.RemoveField(
            model_name='promo',
            name='store_name',
        ),
        migrations.RemoveField(
            model_name='reimbursement',
            name='store_name',
        ),
        migrations.DeleteModel(
            name='AdditionalCommRate',
        ),
        migrations.DeleteModel(
            name='ConcessionalRate',
        ),
        migrations.DeleteModel(
            name='DefaultRate',
        ),
        migrations.DeleteModel(
            name='DeliveryZone',
        ),
        migrations.DeleteModel(
            name='Penalty',
        ),
        migrations.DeleteModel(
            name='Penalty_orders',
        ),
        migrations.DeleteModel(
            name='Promo',
        ),
        migrations.DeleteModel(
            name='Reimbursement',
        ),
    ]
