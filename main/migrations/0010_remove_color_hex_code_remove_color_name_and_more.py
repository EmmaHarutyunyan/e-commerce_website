# Generated by Django 5.1 on 2025-01-29 15:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_color_product_colors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='color',
            name='hex_code',
        ),
        migrations.RemoveField(
            model_name='color',
            name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='colors',
        ),
        migrations.AddField(
            model_name='color',
            name='color_code',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='color',
            name='color_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='color',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='colors', to='main.product'),
        ),
    ]
