# Generated by Django 5.0 on 2024-05-30 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense_management', '0006_alter_expense_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='date',
            new_name='datetime',
        ),
    ]
