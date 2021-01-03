# Generated by Django 3.1 on 2020-12-19 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_feeding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeding',
            name='date',
            field=models.DateField(verbose_name='Feeding Date'),
        ),
        migrations.AlterField(
            model_name='feeding',
            name='meal',
            field=models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner')], default='B', max_length=1),
        ),
    ]
