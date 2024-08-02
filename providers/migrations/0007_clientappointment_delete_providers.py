# Generated by Django 4.2.2 on 2024-06-05 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0006_department_details_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('time_of_appointment', models.TimeField()),
                ('date_of_appointment', models.DateField()),
                ('location', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('reason_for_appointment', models.TextField()),
                ('doctor_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to='providers.doctor')),
            ],
        ),
        migrations.DeleteModel(
            name='Providers',
        ),
    ]
