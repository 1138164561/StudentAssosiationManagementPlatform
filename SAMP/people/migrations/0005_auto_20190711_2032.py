# Generated by Django 2.2.1 on 2019-07-11 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20190710_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='cookie_id',
            field=models.CharField(max_length=256, null=True),
        ),
    ]