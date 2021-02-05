# Generated by Django 3.0.8 on 2021-02-05 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('shop', '0005_product_barcode_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellerProductStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_count', models.IntegerField(default=0)),
                ('product_ps', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Product')),
                ('seller_ps', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Seller')),
            ],
        ),
    ]
