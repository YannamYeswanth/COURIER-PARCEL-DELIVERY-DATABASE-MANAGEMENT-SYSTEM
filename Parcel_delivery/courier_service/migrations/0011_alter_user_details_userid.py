# Generated by Django 4.2.2 on 2023-10-21 08:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('courier_service', '0010_alter_user_details_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='UserId',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]