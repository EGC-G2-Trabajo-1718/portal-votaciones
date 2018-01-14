# coding=utf-8
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

    def test_lugaresGeograficos(self):
        self.assertEqual(parsingDeFicheros.parseLugaresGeograficos('ciudades'),(['huelva', 'sevilla', 'cadiz', 'cordoba', 'jaen', 'almeria', 'granada', 'malaga', 'vigo', 'orense', 'la_corunia', 'pontevedra'], [416, 49, 100, 211, 10, 198, 154, 259, 456, 146, 373, 645]))
        self.assertEqual(parsingDeFicheros.parseLugaresGeograficos('paises'),(['Espa\xc3\xb1a', 'Rusia', 'Portugal', 'Francia', 'Italia', 'Estados Unidos', 'Colombia', 'Brasil', 'Alemania', 'Chile', 'Ruman\xc3\xada', 'Estonia'], [416, 49, 100, 211, 10, 198, 154, 259, 456, 146, 373, 645]))

    def test_obtenerCensoYVotantes(self):
        self.assertEqual(parsingDeFicheros.obtener_censo(None,None),1345)
        self.assertEqual(parsingDeFicheros.obtener_votantes(None,None),532)

    def test_votosPorOpcion(self):
        self.assertEqual(parsingDeFicheros.votosPorOpcionNuevaApi(None,None),(['Juan', 'Ana', 'Pepe', 'Luis', 'Nulo', 'Blanco'], [179, 176, 156, 141, 168, 129]))


    def test_votosPorTramoHorario(self):
        self.assertEqual(parsingDeFicheros.votosPorTramoHorario(),(['00:00 - 05:00', '05:00 - 10:00', '10:00 - 15:00', '15:00 - 20:00', '20:00 - 24:00'], [8, 14, 8, 0, 0]))