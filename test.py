import unittest
import parsingDeFicheros


class test_unitarios(unittest.TestCase):
    def test_extraccion_datos(self):
        self.assertIsNotNone(parsingDeFicheros.extraccion_datos('http://localhost:3000/edades'))
        self.assertIsNotNone(parsingDeFicheros.extraccion_datos('http://localhost:3000/ciudades'))
        self.assertIsNotNone(parsingDeFicheros.extraccion_datos('http://localhost:3000/provincias'))
        self.assertIsNotNone(parsingDeFicheros.extraccion_datos('http://localhost:3000/comunidades'))
        self.assertIsNotNone(parsingDeFicheros.extraccion_datos('http://localhost:3000/paises'))
        self.assertIsNotNone(parsingDeFicheros.extraccion_datos('http://localhost:3000/recuentoDatosCompletos'))
        self.assertIsNotNone(parsingDeFicheros.extraccion_datos('http://localhost:3000/recuentoResultados'))

    def test_parseEdades(self):
        self.assertEqual(parsingDeFicheros.parseEdades(),(['18-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90+'], [4, 15, 17, 9, 6, 12, 15, 0, 0]))

    