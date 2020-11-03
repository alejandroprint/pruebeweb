#from django.test import TestCase

# Create your tests here.
import unittest
from web.models import producto


class testproducto(unittest.TestCase):

    def test_crear_producto(self):
        Producto = producto.objects.create(
                                           codigo='12345',
                                           marca='iphone',
                                           modelo='xsmax',
                                           descripcion='elmejormodelo',
                                           precio='$699.990',
                                           tipo='c',
                                           activo=1,
                                           destacado=1
                                           )
        Producto.save()

        self.assertTrue(Producto,True)

    def test_val_codigo(self):
        Producto = producto.objects.get(codigo='12345')
        self.assertEquals(Producto.codigo,'12345')

    def test_crear_demo(self):
        a = 1
        self.assertEqual(a, 1)