# Generated by Django 4.1.3 on 2023-01-19 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Folder', '0002_auto_20221222_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
