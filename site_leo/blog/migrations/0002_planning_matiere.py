# Generated by Django 4.2.2 on 2023-08-11 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planning',
            name='matiere',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
