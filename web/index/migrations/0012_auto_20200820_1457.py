# Generated by Django 3.0.7 on 2020-08-20 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_newevilfunc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newevilfunc',
            name='origin_func_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]