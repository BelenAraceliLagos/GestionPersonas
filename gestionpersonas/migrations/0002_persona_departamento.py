# Generated by Django 5.1.2 on 2024-10-19 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionpersonas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='departamento',
            field=models.CharField(default=1995, max_length=100, verbose_name='depto'),
            preserve_default=False,
        ),
    ]
