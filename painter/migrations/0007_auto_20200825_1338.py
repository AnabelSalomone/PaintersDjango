# Generated by Django 2.2.15 on 2020-08-25 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painter', '0006_auto_20200825_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painter',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
