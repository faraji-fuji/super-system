# Generated by Django 4.2.4 on 2023-08-20 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255)),
                ('role_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='VendorStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_id', models.CharField(max_length=255)),
                ('user_id', models.CharField(max_length=255)),
                ('role_id', models.CharField(max_length=255)),
            ],
        ),
    ]
