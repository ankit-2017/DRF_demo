# Generated by Django 3.0.6 on 2020-05-27 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detectedfile',
            old_name='Date',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='detectedfile',
            name='count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
