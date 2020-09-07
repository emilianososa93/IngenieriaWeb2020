# Generated by Django 3.1 on 2020-09-05 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


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
                ('tipoPublicacion', models.CharField(blank=True, choices=[('Primario', 'Primario'), ('Secundario', 'Secundario'), ('Universitarios', 'Universitarios')], max_length=50, null=True)),
                ('estadoPublicacion', models.CharField(blank=True, choices=[('Publicado', 'Publicado'), ('Borrador', 'Borrador'), ('Denunciado', 'Denunciado'), ('Eliminado', 'Eliminado')], max_length=50, null=True)),
                ('Contenido', models.TextField()),
                ('precio', models.TextField()),
                ('FechaPublicacion', models.DateField(auto_now=True, verbose_name='Date')),
                ('FechaBajaPublicacion', models.DateField(default=None, editable=False, null=True)),
                ('FechaModificacionPublicacion', models.DateField(default=None, editable=False, null=True)),
                ('idUsuarioPublicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]