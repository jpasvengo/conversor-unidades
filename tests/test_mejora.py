"""
Pruebas unitarias para la mejora de intercambiar unidades y lógica de conversión (Issue #1).
"""

import unittest
from logica_conversor import convertir, intercambiar_unidades, formatear_resultado


class TestMejoraIntercambiarUnidades(unittest.TestCase):

    def test_intercambiar_unidades_basico(self):
        """Verifica que mm -> m pasa a ser m -> mm."""
        origen = "Milímetros (mm)"
        destino = "Metros (m)"
        nuevo_origen, nuevo_destino = intercambiar_unidades(origen, destino)

        self.assertEqual(nuevo_origen, "Metros (m)")
        self.assertEqual(nuevo_destino, "Milímetros (mm)")

    def test_intercambiar_dos_veces_restaura(self):
        """Pulsar dos veces intercambiar unidades debe restaurar el estado original."""
        origen = "Pulgadas (in)"
        destino = "Centímetros (cm)"

        o1, d1 = intercambiar_unidades(origen, destino)
        o2, d2 = intercambiar_unidades(o1, d1)

        self.assertEqual(o2, origen)
        self.assertEqual(d2, destino)

    def test_conversion_precision(self):
        """Comprueba que la conversión matemática sigue funcionando correctamente."""
        # 1 metro = 1000 milímetros
        self.assertAlmostEqual(convertir(1.0, "Metros (m)", "Milímetros (mm)"), 1000.0)
        # 1000 milímetros = 1 metro
        self.assertAlmostEqual(convertir(1000.0, "Milímetros (mm)", "Metros (m)"), 1.0)
        # 1 pulgada = 2.54 cm
        self.assertAlmostEqual(convertir(1.0, "Pulgadas (in)", "Centímetros (cm)"), 2.54)
        # 1 pie = 12 pulgadas (0.3048 m / 0.0254 m = 12)
        self.assertAlmostEqual(convertir(1.0, "Pies (ft)", "Pulgadas (in)"), 12.0)

    def test_formatear_resultado(self):
        """Comprueba el formato legible de los resultados."""
        self.assertEqual(formatear_resultado(15.0), "15")
        self.assertEqual(formatear_resultado(15.25), "15.25")


if __name__ == "__main__":
    unittest.main()
