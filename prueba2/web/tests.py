from django.test import TestCase

# Create your tests here.
import unittest
from web.models import producto


class testproducto(unittest.TestCase):

    def test_crear_objeto(self):
        producto = producto.objects.create(
                                           codigo='003',
                                           marca='iphone',
                                           modelo='xs max',
                                           descripcion='el mejor modelo del mundo',
                                           precio='$699.990',
                                           activo=1,
                                           tipo='c',
                                           destacado=1
                                           )
        producto.save()

        self.assertTrue(producto,True)

    def test_val_rut(self):
        producto = producto.objects.get(codigo='003')
        self.assertEquals(producto.codigo, '003')

    def test_crear_demo(self):
        a = 1
        self.assertEqual(a, 1)