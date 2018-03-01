# Generated by Django 2.0.1 on 2018-02-12 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0024_auto_20180212_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalcommrate',
            name='store_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapping.OcStorelocatorStore'),
        ),
        migrations.AlterField(
            model_name='concessionalrate',
            name='store_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapping.OcStorelocatorStore'),
        ),
        migrations.AlterField(
            model_name='defaultrate',
            name='store_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapping.OcStorelocatorStore'),
        ),
        migrations.AlterField(
            model_name='deliveryzone',
            name='store_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapping.OcStorelocatorStore'),
        ),
        migrations.AlterField(
            model_name='penalty',
            name='store_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapping.OcStorelocatorStore'),
        ),
        migrations.AlterField(
            model_name='promo',
            name='store_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapping.OcStorelocatorStore'),
        ),
        migrations.AlterField(
            model_name='reimbursement',
            name='store_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapping.OcStorelocatorStore'),
        ),
    ]
