# Generated by Django 2.0 on 2019-09-05 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=50)),
                ('limitby', models.CharField(choices=[('quota', 'quota')], default='quota', max_length=20)),
            ],
            options={
                'db_table': 'groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='groupsmembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'groupsmembers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='printers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('printername', models.CharField(max_length=30, verbose_name='Nombre de la impresora')),
                ('description', models.CharField(max_length=50, verbose_name='Descripcion')),
                ('priceperpage', models.FloatField(default=0.5)),
                ('priceperjob', models.FloatField(default=0)),
                ('passthrough', models.CharField(choices=[('f', 'f')], default='f', max_length=20)),
                ('maxjobsize', models.FloatField(default=0)),
            ],
            options={
                'db_table': 'printers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='userpquota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lifepagecounter', models.IntegerField(default=0)),
                ('pagecounter', models.IntegerField(default=0)),
                ('softlimit', models.IntegerField(default=0, verbose_name='Limite blando')),
                ('hardlimit', models.IntegerField(default=0, verbose_name='Limite duro')),
                ('datelimit', models.DateTimeField(null=True)),
                ('maxjobsize', models.IntegerField(null=True)),
                ('warncount', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'userpquota',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, verbose_name='Nombre de usuario')),
                ('email', models.CharField(max_length=100)),
                ('balance', models.FloatField(default=0)),
                ('lifetimepaid', models.DateTimeField(null=True, verbose_name='Tiempo de pago')),
                ('description', models.CharField(max_length=100, verbose_name='Descripcion')),
                ('overcharge', models.IntegerField(default=1)),
                ('level', models.CharField(max_length=15, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]
