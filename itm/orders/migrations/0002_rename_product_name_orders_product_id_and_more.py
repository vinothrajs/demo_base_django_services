# Generated by Django 5.0.3 on 2024-04-22 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='product_name',
            new_name='product_id',
        ),
        migrations.AlterField(
            model_name='inventory',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='orders',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='orders',
            name='total_amount',
            field=models.IntegerField(),
        ),
    ]