# Generated by Django 5.0 on 2024-05-29 13:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_management', '0005_alter_expensecategory_options_expensecategory_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expense_management.expensecategory'),
        ),
    ]
