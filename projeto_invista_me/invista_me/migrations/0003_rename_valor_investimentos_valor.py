# Generated by Django 5.0.4 on 2024-05-08 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invista_me', '0002_rename_investimento_investimentos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investimentos',
            old_name='valor',
            new_name='Valor',
        ),
    ]
