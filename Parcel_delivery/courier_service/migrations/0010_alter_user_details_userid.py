# Generated by Django 4.2.2 on 2023-10-21 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier_service', '0009_alter_user_details_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='UserId',
            field=models.UUIDField(),
        ),
    ]
