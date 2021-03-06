# Generated by Django 3.1 on 2020-10-13 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('idPublicacion', models.AutoField(primary_key=True, serialize=False)),
                ('tituloPublicacion', models.CharField(max_length=50)),
                ('tipoPublicacion', models.CharField(blank=True, choices=[('Primario', 'Nivel Primario'), ('Secundario', 'Nivel Secundario'), ('Universitarios', 'Nivel Universitarios')], max_length=50, null=True)),
                ('estadoPublicacion', models.CharField(blank=True, choices=[('Publicado', 'Publicado'), ('Borrador', 'Borrador'), ('Eliminado', 'Eliminado')], max_length=50, null=True)),
                ('ubicacionGeografica', models.TextField(blank=True, max_length=50, null=True)),
                ('materia', models.CharField(choices=[('Matemáticas', 'Matemáticas'), ('Sociales', 'Ciencias Sociales'), ('Naturales', 'Ciencias Naturales'), ('Lengua', 'Lengua'), ('InglesI', 'InglésI'), ('InglesII', 'InglésII'), ('InglesIII', 'InglésIII'), ('Literatura', 'Literatura'), ('Historia', 'Historia'), ('Química', 'Química'), ('Informática', 'Informática')], max_length=50, null=True)),
                ('Contenido', models.TextField()),
                ('precio', models.TextField()),
                ('FechaPublicacion', models.DateField(auto_now=True, verbose_name='Date')),
                ('FechaBajaPublicacion', models.DateField(default=None, editable=False, null=True)),
                ('FechaModificacionPublicacion', models.DateField(default=None, editable=False, null=True)),
                ('idUsuarioPublicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudContacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estadoSolicitud', models.CharField(blank=True, choices=[('Pendiente', 'Pendiente'), ('Rechazado', 'Rechazado'), ('Aceptado', 'Aceptado')], max_length=50, null=True)),
                ('idPublicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sitio.publicacion')),
                ('idUsuarioReceptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_receive', to=settings.AUTH_USER_MODEL)),
                ('idUsuarioSolicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_create', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=1000, null=True)),
                ('fechaComentario', models.DateField(default=django.utils.timezone.now, null=True)),
                ('fechaBajaComentario', models.DateField(null=True)),
                ('motivoBaja', models.CharField(max_length=500)),
                ('estadoComentario', models.CharField(blank=True, choices=[('Publicado', 'Publicado'), ('Borrador', 'Borrador'), ('Denunciado', 'Denunciado'), ('Eliminado', 'Eliminado')], default='Borrador', max_length=20)),
                ('idpublicacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Sitio.publicacion')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
