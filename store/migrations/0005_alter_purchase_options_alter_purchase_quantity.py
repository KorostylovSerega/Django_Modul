# Generated by Django 4.1.3 on 2022-11-14 09:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_returnpurchase_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchase',
            options={'ordering': ['-date'], 'verbose_name': 'purchase', 'verbose_name_plural': 'purchases'},
        ),
        migrations.AlterField(
            model_name='purchase',
            name='quantity',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
