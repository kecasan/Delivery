# Generated by Django 5.0.6 on 2024-05-09 13:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_alter_pedido_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 9, 10, 56, 1, 456704)),
        ),
    ]
