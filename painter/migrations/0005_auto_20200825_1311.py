# Generated by Django 2.2.15 on 2020-08-25 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painter', '0004_auto_20200825_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='painter',
            name='picture',
        ),
        migrations.AlterField(
            model_name='painter',
            name='country',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='painter',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='painter',
            name='surname',
            field=models.CharField(max_length=200),
        ),
    ]
