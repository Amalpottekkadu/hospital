# Generated by Django 4.1.3 on 2022-11-15 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=100)),
                ('doc_spec', models.CharField(max_length=250)),
                ('doc_image', models.ImageField(upload_to='doctors')),
                ('dpt_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.departments')),
            ],
        ),
    ]
