# Generated by Django 3.2.7 on 2021-09-20 09:34
import django.utils.timezone
from django.db import migrations, models


def set_default_checkout_line_currency(apps, schema_editor):
    CheckoutLine = apps.get_model("checkout", "CheckoutLine")
    for checkout_line in CheckoutLine.objects.all().iterator():
        checkout_line.currency = checkout_line.checkout.currency
        checkout_line.save(update_fields=["currency"])


class Migration(migrations.Migration):
    dependencies = [
        ("checkout", "0039_alter_checkout_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="checkout",
            name="price_expiration",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="checkout",
            name="shipping_price_gross_amount",
            field=models.DecimalField(decimal_places=3, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name="checkout",
            name="shipping_price_net_amount",
            field=models.DecimalField(decimal_places=3, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name="checkout",
            name="subtotal_gross_amount",
            field=models.DecimalField(decimal_places=3, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name="checkout",
            name="subtotal_net_amount",
            field=models.DecimalField(decimal_places=3, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name="checkout",
            name="total_gross_amount",
            field=models.DecimalField(decimal_places=3, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name="checkout",
            name="total_net_amount",
            field=models.DecimalField(decimal_places=3, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name="checkoutline",
            name="currency",
            field=models.CharField(null=True, max_length=3),
        ),
        migrations.RunPython(set_default_checkout_line_currency),
        migrations.AlterField(
            model_name="checkoutline",
            name="currency",
            field=models.CharField(max_length=3),
        ),
        migrations.AddField(
            model_name="checkoutline",
            name="total_price_gross_amount",
            field=models.DecimalField(decimal_places=3, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name="checkoutline",
            name="total_price_net_amount",
            field=models.DecimalField(decimal_places=3, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name="checkoutline",
            name="unit_price_gross_amount",
            field=models.DecimalField(decimal_places=3, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name="checkoutline",
            name="unit_price_net_amount",
            field=models.DecimalField(decimal_places=3, default=0, max_digits=12),
        ),
    ]
