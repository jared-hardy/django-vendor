# Generated by Django 3.1.3 on 2020-11-20 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0010_auto_20201112_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_1',
            field=models.CharField(max_length=40, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_2',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Address 2 (Optional)'),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.IntegerField(choices=[(581, 'United States')], default=581, verbose_name='Country/Region'),
        ),
    ]