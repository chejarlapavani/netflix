# Generated by Django 4.2.7 on 2024-01-02 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.genre'),
        ),
    ]
