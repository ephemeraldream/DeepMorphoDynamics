# Generated by Django 5.0.3 on 2024-04-29 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymorpho', '0003_embryo_name_alter_embryo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='embryoint',
            name='class_type',
            field=models.IntegerField(blank=True, choices=[(0, 'Zero'), (1, 'First'), (2, 'Second'), (3, 'Third')], null=True, verbose_name='Метка класса'),
        ),
    ]