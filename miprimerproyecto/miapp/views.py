from django.shortcuts import render

from .models import Estudiante


def main(request):

    # Verificamos que en la base de datos no exista ningun registro
    if Estudiante.objects.all().count() == 0:
        estudiante_uno = Estudiante()
        estudiante_uno.name = 'Goku'
        estudiante_uno.apellido = 'Son'
        estudiante_uno.save()

        estudiante_dos = Estudiante()
        estudiante_dos.name = 'Naruto'
        estudiante_dos.apellido = 'Uzumaki'
        estudiante_dos.save()

    estudiantes = Estudiante.objects.all()
    return render(request, 'main.html', {'estudiantes': estudiantes})
