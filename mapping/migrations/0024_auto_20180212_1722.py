# Generated by Django 2.0.1 on 2018-02-12 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0023_auto_20180209_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concessionalrate',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mapping.OcCategory'),
        ),
    ]
