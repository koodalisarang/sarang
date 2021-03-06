# Generated by Django 2.2.5 on 2019-11-29 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_busket'),
    ]

    operations = [
        migrations.CreateModel(
            name='amount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(max_length=10)),
                ('date', models.DateField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(max_length=10)),
                ('itemid', models.IntegerField()),
                ('itemname', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('total', models.IntegerField()),
                ('date', models.DateField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
