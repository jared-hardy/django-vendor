# Generated by Django 3.1.1 on 2020-09-10 23:34

import autoslug.fields
import django.contrib.sites.managers
from django.db import migrations, models
import django.db.models.manager
import uuid
import vendor.models.base


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=80, verbose_name='Name')),
            ],
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='last updated')),
                ('sku', models.CharField(blank=True, help_text='User Defineable SKU field', max_length=40, null=True, unique=True, verbose_name='SKU')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=80, verbose_name='Name')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique_with=('site__id',))),
                ('available', models.BooleanField(default=False, help_text='Is this currently available?', verbose_name='Available')),
                ('description', models.JSONField(blank=True, default=dict, null=True, verbose_name='Description')),
                ('meta', models.JSONField(blank=True, default=vendor.models.base.product_meta_default, help_text="Eg: { 'msrp':{'usd':10.99} }\n(iso4217 Country Code):(MSRP Price)", null=True, verbose_name='Meta')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
    ]