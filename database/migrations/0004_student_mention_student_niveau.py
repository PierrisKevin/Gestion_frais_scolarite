# Generated by Django 4.1.5 on 2023-03-05 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_alter_administrator_photoprofil_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='mention',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='niveau',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
    ]