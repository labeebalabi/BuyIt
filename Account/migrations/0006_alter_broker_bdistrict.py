# Generated by Django 4.2.4 on 2023-09-01 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0005_broker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broker',
            name='Bdistrict',
            field=models.CharField(choices=[('kasarkode', 'kasarkode'), ('kannur', 'kannur'), ('kozhikode', 'kozhikode'), ('malappuram', 'malappuram'), ('wayanad', 'wayanad'), ('palakkad', 'palakkad'), ('idukki', 'idukki'), ('thrissur', 'thrissur'), ('eranakulam', 'eranakulam'), ('alappuzha', 'alappuzha'), ('pathanamthitta', 'pathanamthitta'), ('kollam', 'kollam'), ('kottayam', 'kottayam'), ('thiruvananthapuram', 'thiruvananthapuram')], default='kannur', max_length=100),
        ),
    ]
