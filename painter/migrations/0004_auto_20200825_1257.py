# Generated by Django 2.2.15 on 2020-08-25 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painter', '0003_auto_20200825_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painter',
            name='country',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='painter',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='painter',
            name='surname',
            field=models.TextField(),
        ),
    ]
