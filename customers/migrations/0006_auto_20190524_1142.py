# Generated by Django 2.2.1 on 2019-05-24 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_auto_20190524_1137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='cutomer_id',
            new_name='customer_id',
        ),
    ]
