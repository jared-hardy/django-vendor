# Generated by Django 3.1.3 on 2020-11-11 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0008_offer_allow_multiple'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='terms',
            field=models.IntegerField(choices=[(0, 'Perpetual'), (10, 'Subscription'), (11, 'Monthly Subscription'), (12, 'Quarterly Subscription'), (13, 'Semi-Annual Subscription'), (14, 'Annual Subscription'), (20, 'One-Time Use')], default=0, verbose_name='Terms'),
        ),
    ]
