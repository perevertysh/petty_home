# Generated by Django 2.2.7 on 2019-12-19 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petdocs', '0003_auto_20191219_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='reg_num',
            field=models.CharField(auto_created=True, max_length=256, null=True, verbose_name='Регистрационный номер'),
        ),
    ]
