# Generated by Django 4.2.7 on 2024-01-15 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskdb',
            name='Due_date',
            field=models.DateTimeField(null=True),
        ),
    ]
