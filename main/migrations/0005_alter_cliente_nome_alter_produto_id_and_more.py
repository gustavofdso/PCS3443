# Generated by Django 4.0.5 on 2022-07-01 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_produto_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='produto',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='venda',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vendedor',
            name='nome',
            field=models.CharField(max_length=300),
        ),
    ]
