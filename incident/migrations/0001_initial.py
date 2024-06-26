# Generated by Django 4.1.1 on 2022-09-21 10:50

import datetime
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
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incident_id', models.CharField(max_length=12, unique=True)),
                ('incident_detail', models.CharField(blank=True, max_length=5000, null=True)),
                ('priority', models.CharField(choices=[('H', 'HIGH'), ('M', 'MEDIUM'), ('L', 'LOW')], default='L', max_length=6)),
                ('incident_status', models.CharField(choices=[('O', 'OPEN'), ('P', 'IN PROGRESS'), ('C', 'CLOSED')], default='O', max_length=15)),
                ('report_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('reporter_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
