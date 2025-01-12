# Generated by Django 5.0.4 on 2024-04-22 05:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tourApp', '0001_initial'),
        ('userApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='activitiesModel',
            fields=[
                ('activities_id', models.CharField(default=None, max_length=60, primary_key=True, serialize=False)),
                ('activities_name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('activities_is_active', models.BooleanField(default=True)),
                ('activities_created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'activities_tb',
            },
        ),
        migrations.CreateModel(
            name='amenitiesModel',
            fields=[
                ('amenities_id', models.CharField(default=None, max_length=60, primary_key=True, serialize=False)),
                ('amenities_name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('amenities_is_active', models.BooleanField(default=True)),
                ('amenities_created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'amenities_tb',
            },
        ),
        migrations.CreateModel(
            name='roomTypeModel',
            fields=[
                ('roomType_id', models.CharField(default=None, max_length=60, primary_key=True, serialize=False)),
                ('roomType_name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('roomType_is_active', models.BooleanField(default=True)),
                ('roomType_created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'roomType_tb',
            },
        ),
        migrations.CreateModel(
            name='serviceModel',
            fields=[
                ('service_id', models.CharField(default=None, max_length=60, primary_key=True, serialize=False)),
                ('service_name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('service_is_active', models.BooleanField(default=True)),
                ('service_created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'service_tb',
            },
        ),
        migrations.CreateModel(
            name='destinationHotelModel',
            fields=[
                ('destinationHotel_id', models.CharField(default=None, max_length=60, primary_key=True, serialize=False)),
                ('destinationHotel_hotel_name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('destinationHotel_hotel_price', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('destinationHotel_hotel_discount', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('destinationHotel_parking', models.BooleanField(default=False)),
                ('destinationHotel_wifi', models.BooleanField(default=True)),
                ('destinationHotel_eating', models.BooleanField(default=True)),
                ('destinationHotel_cooling', models.BooleanField(default=True)),
                ('destinationHotel_only_adults', models.BooleanField(default=False)),
                ('destinationHotel_pet_allowed', models.BooleanField(default=False)),
                ('destinationHotel_is_active', models.BooleanField(default=True)),
                ('destinationHotel_created_at', models.DateTimeField(auto_now_add=True)),
                ('Destinationstay', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tourApp.destinationstaymodel')),
            ],
            options={
                'db_table': 'destinationHotel_tb',
            },
        ),
        migrations.CreateModel(
            name='destinationHotelImageModel',
            fields=[
                ('destinationHotelImage_id', models.CharField(default=None, max_length=60, primary_key=True, serialize=False)),
                ('destinationHotelImage_image', models.ImageField(upload_to='hotel/')),
                ('destinationHotelImage_is_active', models.BooleanField(default=True)),
                ('destinationHotelImage_created_at', models.DateTimeField(auto_now_add=True)),
                ('destinationHotel', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hotelApp.destinationhotelmodel')),
            ],
            options={
                'db_table': 'hotel_tb',
            },
        ),
        migrations.CreateModel(
            name='hotelActivitiesModel',
            fields=[
                ('hotelActivities_id', models.CharField(default=None, max_length=60, primary_key=True, serialize=False)),
                ('hotelActivities_is_active', models.BooleanField(default=True)),
                ('hotelActivities_created_at', models.DateTimeField(auto_now_add=True)),
                ('activities', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hotelApp.activitiesmodel')),
                ('destinationHotel', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hotelApp.destinationhotelmodel')),
            ],
            options={
                'db_table': 'hotelActivities_tb',
            },
        ),
        migrations.CreateModel(
            name='hotelAmenitiesModel',
            fields=[
                ('hotelAmenities_id', models.CharField(default=None, max_length=60, primary_key=True, serialize=False)),
                ('hotelAmenities_is_active', models.BooleanField(default=True)),
                ('hotelAmenities_created_at', models.DateTimeField(auto_now_add=True)),
                ('amenities', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hotelApp.amenitiesmodel')),
                ('destinationHotel', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hotelApp.destinationhotelmodel')),
            ],
            options={
                'db_table': 'hotelAmenities_tb',
            },
        ),
        migrations.CreateModel(
            name='hotelRoomTypeModel',
            fields=[
                ('hotelRoomType_id', models.CharField(default=None, max_length=60, primary_key=True, serialize=False)),
                ('hotelRoomType_is_active', models.BooleanField(default=True)),
                ('hotelRoomType_created_at', models.DateTimeField(auto_now_add=True)),
                ('destinationHotel', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hotelApp.destinationhotelmodel')),
                ('roomType', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hotelApp.roomtypemodel')),
            ],
            options={
                'db_table': 'hotelRoomType_tb',
            },
        ),
        migrations.CreateModel(
            name='hotelServiceModel',
            fields=[
                ('hotelService_id', models.CharField(default=None, max_length=60, primary_key=True, serialize=False)),
                ('hotelService_is_active', models.BooleanField(default=True)),
                ('hotelService_created_at', models.DateTimeField(auto_now_add=True)),
                ('destinationHotel', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hotelApp.destinationhotelmodel')),
                ('service', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hotelApp.servicemodel')),
            ],
            options={
                'db_table': 'hotelService_tb',
            },
        ),
        migrations.CreateModel(
            name='userGuestModel',
            fields=[
                ('userGuest_id', models.CharField(default=None, max_length=60, primary_key=True, serialize=False)),
                ('userGuest_firstname', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('userGuest_lastname', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('userGuest_dateofbirth', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('userGuest_gender', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('userGuest_passport_number', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('userGuest_passport_expire', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('userGuest_nationality', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('userGuest_created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='userApp.signupmodel')),
            ],
            options={
                'db_table': 'userGuest_tb',
            },
        ),
        migrations.CreateModel(
            name='userHotelModel',
            fields=[
                ('userHotel_id', models.CharField(default=None, max_length=60, primary_key=True, serialize=False)),
                ('userHotel_check_in_date', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('userHotel_check_out_date', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('userHotel_check_in_period', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('userHotel_check_out_period', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('userHotel_totallenghtostay', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('userHotel_totalmembers', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('userHotel_nationality', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('userHotel_created_at', models.DateTimeField(auto_now_add=True)),
                ('destinationHotel', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hotelApp.destinationhotelmodel')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='userApp.signupmodel')),
                ('userGuest', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hotelApp.userguestmodel')),
            ],
            options={
                'db_table': ' userHotel_tb',
            },
        ),
    ]
