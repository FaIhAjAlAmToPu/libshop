# Generated by Django 5.2 on 2025-04-20 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraries', '0002_alter_store_address_alter_store_contents_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
