# Generated by Django 3.2.14 on 2022-07-22 20:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('booking_number', models.BigAutoField(primary_key=True, serialize=False)),
                ('adults', models.SmallIntegerField()),
                ('children', models.SmallIntegerField(blank=True, null=True)),
                ('highchairs', models.SmallIntegerField(blank=True, null=True)),
                ('payment', models.IntegerField(choices=[(0, 'Not Paid'), (1, 'Payment Accepted')], default=0)),
                ('additional_info', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('reference_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('food', models.CharField(choices=[('M', 'Meat'), ('V', 'Vegetarian'), ('C', 'Child')], max_length=1)),
                ('dairy', models.BooleanField(default=False)),
                ('gluten', models.BooleanField(default=False)),
                ('nuts', models.BooleanField(default=False)),
                ('peanuts', models.BooleanField(default=False)),
                ('egg', models.BooleanField(default=False)),
                ('shellfish', models.BooleanField(default=False)),
                ('soy', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.book')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
