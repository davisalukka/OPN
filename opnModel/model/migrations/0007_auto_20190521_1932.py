# Generated by Django 2.1.3 on 2019-05-21 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0006_valuationmetrics_industryvertical'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valuationmetrics',
            name='industryVertical',
            field=models.CharField(default='', max_length=150),
        ),
    ]
