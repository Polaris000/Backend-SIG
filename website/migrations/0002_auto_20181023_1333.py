# Generated by Django 2.1.1 on 2018-10-23 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='data',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
