# Generated by Django 3.1 on 2020-10-11 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sitio', '0007_auto_20200929_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='estadoPublicacion',
            field=models.CharField(blank=True, choices=[('Publicado', 'Publicado'), ('Borrador', 'Borrador'), ('Eliminado', 'Eliminado')], max_length=50, null=True),
        ),
    ]