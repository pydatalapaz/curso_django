from django.db import models


class Estudiante(models.Model):
    name = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return '{} {}'.format(self.name, self.apellido)
