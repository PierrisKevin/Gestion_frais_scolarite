# Generated by Django 4.1.5 on 2023-03-01 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('photoProfil', models.ImageField(upload_to='img_admin')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('prenom', models.CharField(max_length=250)),
                ('date_naissance', models.DateField()),
                ('lieu_naissance', models.CharField(max_length=150)),
                ('adresse', models.CharField(max_length=150)),
                ('photoEtudiant', models.ImageField(upload_to='img_student')),
                ('add_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='add-+', to='database.administrator')),
            ],
        ),
        migrations.CreateModel(
            name='paiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('premier', models.BooleanField(default=False)),
                ('second', models.BooleanField(default=False)),
                ('student_pay', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='database.student')),
            ],
        ),
    ]
