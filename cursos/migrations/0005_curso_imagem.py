# Generated by Django 4.0.5 on 2022-07-07 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0004_alter_aula_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='imagem',
            field=models.URLField(blank=True, null=True),
        ),
    ]
