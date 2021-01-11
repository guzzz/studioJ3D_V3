# Generated by Django 2.1.2 on 2020-01-07 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('space', models.CharField(blank=True, choices=[('living room', 'Sala'), ('bedroom', 'Quarto'), ('home office', 'Escritório'), ('bathroom', 'Banheiro'), ('kitchen', 'Cozinha'), ('outside', 'Externa'), ('frontage', 'Fachada'), ('restaurant', 'Restaurante'), ('corporate', 'Corporativo'), ('tcc', 'TCC')], max_length=15, verbose_name='Ambiente')),
                ('photo', models.FileField(upload_to='', verbose_name='Foto')),
                ('small_photo', models.FileField(null=True, upload_to='', verbose_name='Foto Pequena')),
                ('position', models.PositiveSmallIntegerField(null=True, verbose_name='Posição')),
                ('description', models.CharField(blank=True, max_length=150, null=True, verbose_name='Descrição')),
                ('width', models.PositiveSmallIntegerField(default=0, verbose_name='Largura')),
                ('height', models.PositiveSmallIntegerField(default=0, verbose_name='Altura')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
            ],
            options={
                'verbose_name': 'um Projeto',
                'verbose_name_plural': 'Imagens dos Projetos',
                'ordering': ['-position'],
            },
        ),
    ]