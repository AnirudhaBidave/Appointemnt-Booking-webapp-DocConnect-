# Generated by Django 4.2 on 2023-05-28 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patient_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='patient_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_login_id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=20)),
                ('contact_number', models.IntegerField(max_length=15)),
                ('allergies', models.CharField(max_length=255)),
                ('medical_condition', models.CharField(max_length=255)),
                ('previous_surgeries', models.CharField(max_length=255)),
            ],
        ),
    ]
