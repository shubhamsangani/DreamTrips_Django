# Generated by Django 5.0.4 on 2024-04-22 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactUsModel',
            fields=[
                ('contactUs_id', models.CharField(default=None, max_length=60, primary_key=True, serialize=False)),
                ('contactUs_name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('contactUs_email', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('contactUs_phone', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('contactUs_subject', models.CharField(blank=True, default=None, max_length=250, null=True)),
                ('contactUs_query', models.TextField(blank=True, default=None, null=True)),
                ('contactUs_created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'contactUsmodel_tb',
            },
        ),
    ]