# Generated by Django 4.0.4 on 2022-05-06 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='CPF',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='ToDoList',
        ),
    ]
