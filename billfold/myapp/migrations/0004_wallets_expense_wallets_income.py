# Generated by Django 4.2.7 on 2024-01-19 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_wallets_balance_alter_wallets_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallets',
            name='expense',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='wallets',
            name='income',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
