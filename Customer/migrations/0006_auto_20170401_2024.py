# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-01 20:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Customer', '0005_auto_20170401_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing_Address',
            fields=[
                ('billAddID', models.IntegerField(primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=10)),
                ('street', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customerID', models.IntegerField(primary_key=True, serialize=False)),
                ('fName', models.CharField(max_length=500)),
                ('lName', models.CharField(max_length=100)),
                ('joinDate', models.CharField(max_length=1000)),
                ('emailID', models.CharField(max_length=1000)),
                ('emailNotification', models.BooleanField()),
                ('billType', models.CharField(max_length=20)),
                ('contactNo', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Payment_Method',
            fields=[
                ('pmtMethodID', models.IntegerField(primary_key=True, serialize=False)),
                ('cardNo', models.CharField(max_length=100)),
                ('cardHolderName', models.CharField(max_length=20)),
                ('cardType', models.CharField(max_length=50)),
                ('expDate', models.CharField(max_length=20)),
                ('cvvNo', models.IntegerField()),
                ('customerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Security',
            fields=[
                ('qID', models.IntegerField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=1000)),
                ('answer', models.CharField(max_length=1000)),
                ('customerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Service_Request',
            fields=[
                ('requestID', models.IntegerField(primary_key=True, serialize=False)),
                ('requestType', models.CharField(max_length=500)),
                ('subscriptionDate', models.CharField(max_length=100)),
                ('fulfillmentDate', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
                ('customerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Shipping_Address',
            fields=[
                ('shipAddID', models.IntegerField(primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=10)),
                ('street', models.CharField(max_length=100)),
                ('customerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='billing_address',
            name='PmtMethodID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.Payment_Method'),
        ),
    ]
