# Generated by Django 5.0.4 on 2024-04-22 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignupModel',
            fields=[
                ('user_id', models.CharField(default=None, max_length=60, primary_key=True, serialize=False)),
                ('user_firstname', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('user_lastname', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('user_email', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('user_password', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('user_username', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('user_mobile', models.CharField(blank=True, default=None, max_length=60, null=True)),
                ('user_dateofbirth', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('user_gender', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('user_city', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('user_state', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('user_country', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('user_image', models.TextField(blank=True, default=None, null=True)),
                ('user_is_loggin', models.BooleanField(default=True)),
                ('user_created_at', models.DateTimeField(auto_now_add=True)),
                ('user_created_at_update', models.CharField(blank=True, default=None, max_length=100, null=True)),
            ],
            options={
                'db_table': 'Signup_tb',
            },
        ),
    ]
