# Generated by Django 3.2.14 on 2022-08-09 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0028_auto_20220808_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='additional_info',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
