# Generated by Django 3.0.7 on 2020-06-27 06:44

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='device',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='tempratureReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reading', models.DecimalField(decimal_places=2, max_digits=3)),
                ('readingDateTime', models.DateTimeField(default=datetime.datetime(2020, 6, 27, 6, 44, 52, 927445, tzinfo=utc))),
                ('deviceId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitors.device')),
            ],
        ),
        migrations.CreateModel(
            name='humidityReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reading', models.DecimalField(decimal_places=2, max_digits=3)),
                ('readingDateTime', models.DateTimeField(default=datetime.datetime(2020, 6, 27, 6, 44, 52, 927445, tzinfo=utc))),
                ('deviceId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitors.device')),
            ],
        ),
    ]
