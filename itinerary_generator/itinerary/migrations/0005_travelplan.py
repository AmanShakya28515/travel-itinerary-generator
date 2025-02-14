# Generated by Django 5.1.5 on 2025-02-10 10:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary', '0004_activity_district_hotel_delete_travelplan_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TravelPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=200)),
                ('current_destination', models.CharField(blank=True, max_length=200, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('budget_category', models.CharField(choices=[('Low', 'Low'), ('Mid', 'Mid'), ('High', 'High')], max_length=50)),
                ('itinerary_generated', models.BooleanField(default=False)),
                ('weather_info', models.JSONField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
