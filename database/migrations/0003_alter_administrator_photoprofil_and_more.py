# Generated by Django 4.1.5 on 2023-03-05 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_alter_administrator_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='photoProfil',
            field=models.ImageField(blank=True, null=True, upload_to='img_admin'),
        ),
        migrations.AlterField(
            model_name='student',
            name='photoEtudiant',
            field=models.ImageField(blank=True, null=True, upload_to='img_student'),
        ),
    ]
