# Generated by Django 4.2.4 on 2023-09-02 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0006_alter_broker_bdistrict'),
    ]

    operations = [
        migrations.AddField(
            model_name='broker',
            name='status',
            field=models.BooleanField(default=0),
        ),
    ]
