# Generated by Django 5.0.3 on 2024-03-07 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Holes',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('group_id', models.CharField(max_length=50)),
                ('subgroup_id', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('condition', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ImageWithClassificationPredictions',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('group_id', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('locations', models.TextField()),
                ('classification', models.TextField()),
                ('dimension', models.CharField(max_length=50)),
            ],
        ),
    ]