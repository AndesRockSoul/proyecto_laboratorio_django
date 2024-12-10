from django.test import TestCase
from .models import Laboratorio
from django.urls import reverse


#Realice pruebas unitarias al modelo Laboratorio, donde se verifique:
#● Que los datos en nuestra base de datos simulada coincidan con los que se crearon inicialmente 
#en setUpTestData para un laboratorio dado. 


class LaboratorioModelTest(TestCase):
    def setUp(self):
        # Crear un laboratorio
        self.laboratorio = Laboratorio.objects.create(
            nombre="Prueba de laboratorio",
            ciudad="Santiago",
            pais="Chile"
        )

    def test_model_laboratorio(self):
        self.laboratorio = Laboratorio.objects.get(id=self.laboratorio.id)

        self.assertEqual(self.laboratorio.nombre,"Prueba de laboratorio")
        self.assertEqual(self.laboratorio.ciudad, "Santiago")
        self.assertEqual(self.laboratorio.pais, "Chile")
        

#● La URL para confirmar que devuelve una respuesta HTTP 200 para laboratorio. 
    def test_eliminar_laboratorio_url(self):
        url = reverse('eliminar_laboratorio', kwargs={'laboratorio_id': self.laboratorio.id})
        response = self.client.get(url) #solicitud GET a la URL
        
        self.assertEqual(response.status_code, 200)          #respuesta sea HTTP 200
        

#● verifica que se use la plantilla correcta,
    def test_eliminar_laboratorio_template(self):
        url = reverse('eliminar_laboratorio', kwargs={'laboratorio_id': self.laboratorio.id})
        response = self.client.get(url)
        
        self.assertTemplateUsed(response, 'eliminar_laboratorio.html')   # Verifica que se esta usando la plantilla correcta


# y confirma que el contenido HTML #coincide con lo esperado.
def test_eliminar_laboratorio_content(self):
    url = reverse('eliminar_laboratorio', kwargs={'laboratorio_id': self.laboratorio.id})
    response = self.client.get(url)

    # Verifica que la pregunta inación swe encnetre
    self.assertContains(response, '¿Estás seguro de eliminar este laboratorio?')

    # Verifica que el nombre del laboratorio esté en el contenido (dentro de <strong>)
    self.assertContains(response, '<strong>{}</strong>'.format(self.laboratorio.nombre))

    #verifica el texto completo de la instancia en la plantills esté
    self.assertContains(response, 'Estás seguro que deseas eliminar el laboratorio:" <strong>{}</strong>"'.format(self.laboratorio.nombre))

    # Verifica los otros elementos de la página
    self.assertContains(response, 'Ciudad: {}'.format(self.laboratorio.ciudad))
    self.assertContains(response, 'País: {}'.format(self.laboratorio.pais))
    self.assertContains(response, 'Confirmar eliminación')




"""
python manage.py test: 
S D:\Bootcamp Python fullstack\M7\FINAL DRILLING M7\practica_final_orm_django\config> python manage.py test
Found 3 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...
----------------------------------------------------------------------
Ran 3 tests in 0.052s

OK
Destroying test database for alias 'default'...
"""

