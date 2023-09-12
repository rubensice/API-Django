# Generated by Django 4.2.4 on 2023-08-22 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('air_date', models.CharField(max_length=50, null=True)),
                ('episode', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('type', models.CharField(max_length=50, null=True)),
                ('dimension', models.CharField(max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=50, null=True)),
                ('species', models.CharField(max_length=50, null=True)),
                ('type', models.CharField(max_length=50, null=True)),
                ('gender', models.CharField(max_length=50, null=True)),
                ('origin', models.CharField(max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='meuApp.location')),
            ],
        ),
    ]