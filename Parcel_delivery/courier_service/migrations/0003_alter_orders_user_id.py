# Generated by Django 4.2.2 on 2023-10-21 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courier_service', '0002_remove_orders_salary_alter_orders_order_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='User_Id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='courier_service.user'),
        ),
    ]
