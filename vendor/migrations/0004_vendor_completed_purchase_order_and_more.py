# Generated by Django 4.2.11 on 2024-05-08 06:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_delete_purchaseorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='completed_purchase_order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vendor',
            name='on_time_completed_purchase_order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vendor',
            name='total_purchase_order',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendor_code',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]