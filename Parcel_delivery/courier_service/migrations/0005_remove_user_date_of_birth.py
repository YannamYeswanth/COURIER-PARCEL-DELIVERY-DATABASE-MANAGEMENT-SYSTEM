# Generated by Django 4.2.2 on 2023-10-21 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courier_service', '0004_user_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_of_birth',
        ),
    ]