# Generated by Django 2.0.4 on 2022-12-22 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_testproxy_alter_stock_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stock',
            options={'verbose_name': '在庫', 'verbose_name_plural': '在庫'},
        ),
        migrations.AlterField(
            model_name='stock',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
