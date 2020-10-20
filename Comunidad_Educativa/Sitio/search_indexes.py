from haystack import indexes
from .models import Publicacion


class PublicacionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    titulo = indexes.CharField(model_attr='tituloPublicacion')
    fecha = indexes.DateTimeField(model_attr='FechaPublicacion')
    Contenido = indexes.CharField(model_attr='Contenido')
    idPublicacion = indexes.CharField(model_attr='idPublicacion')
    precio = indexes.CharField(model_attr='precio')

    def get_model(self):
        return Publicacion

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(estadoPublicacion='Publicado')
