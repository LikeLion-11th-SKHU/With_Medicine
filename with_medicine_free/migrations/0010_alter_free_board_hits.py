# Generated by Django 4.2.1 on 2023-08-14 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('with_medicine_free', '0009_alter_free_board_hits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='free_board',
            name='hits',
            field=models.PositiveIntegerField(default=0, verbose_name='조회수'),
        ),
    ]