# Generated by Django 4.2.1 on 2023-08-13 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('with_medicine_free', '0003_alter_free_board_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='free_board',
            name='hits',
            field=models.PositiveIntegerField(default=1, verbose_name='조회수'),
        ),
    ]