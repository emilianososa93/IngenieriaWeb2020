# Generated by Django 3.1 on 2020-10-13 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sitio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitudcontacto',
            name='idPublicacion',
        ),
        migrations.RemoveField(
            model_name='solicitudcontacto',
            name='idUsuarioReceptor',
        ),
        migrations.RemoveField(
            model_name='solicitudcontacto',
            name='idUsuarioSolicitante',
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
        migrations.DeleteModel(
            name='SolicitudContacto',
        ),
    ]
