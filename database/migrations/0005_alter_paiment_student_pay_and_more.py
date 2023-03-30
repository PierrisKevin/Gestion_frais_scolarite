# Generated by Django 4.1.5 on 2023-03-30 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_student_mention_student_niveau'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paiment',
            name='student_pay',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='database.student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='photoEtudiant',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='img_student'),
        ),
    ]
