# Generated by Django 5.0.4 on 2024-04-29 17:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymorpho', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Embryo',
            fields=[
                ('id', models.TextField(max_length=100, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WholeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Ненарезанная целая картинка')),
                ('time', models.IntegerField(verbose_name='Порядковый номер картинки')),
            ],
        ),
        migrations.CreateModel(
            name='EmbryoInT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Нарезанная картинка')),
                ('class_type', models.IntegerField(choices=[(0, 'Zero'), (1, 'First'), (2, 'Second'), (3, 'Third')], verbose_name='Метка класса')),
                ('well_number', models.IntegerField(verbose_name='Номер лунки.')),
                ('embryo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mymorpho.embryo', verbose_name='Название Эмбриона')),
                ('source_image', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mymorpho.wholeimage', verbose_name='Картинка из которой нарезан кадр')),
            ],
        ),
    ]
