# Generated by Django 2.2.13 on 2021-10-05 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rna', '0003_auto_20210930_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='product',
            field=models.CharField(choices=[('Firefox', 'Firefox'), ('Firefox for Android', 'Firefox for Android'), ('Firefox for iOS', 'Firefox for iOS'), ('Firefox Extended Support Release', 'Firefox Extended Support Release'), ('Thunderbird', 'Thunderbird')], max_length=255),
        ),
    ]
