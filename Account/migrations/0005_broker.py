# Generated by Django 4.2.4 on 2023-08-31 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0004_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Broker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bname', models.CharField(max_length=100)),
                ('Bplace', models.CharField(max_length=100)),
                ('Bdistrict', models.CharField(max_length=100)),
                ('Bphone', models.IntegerField(null=True)),
                ('Bage', models.IntegerField(null=True)),
            ],
        ),
    ]
