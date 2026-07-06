# PRUEBAS UNITARIAS EN PYTHON — UNITTEST

import unittest
import cambia_texto  # módulo externo que contiene la función a probar

class ProbarCambiaTexto(unittest.TestCase):
    # Caso de prueba: verificar que la función convierte a mayúsculas
    def test_todo_mayuscula(self):
        self.assertEqual(cambia_texto.todo_mayuscula('hola'), 'HOLA')

# Ejecutar pruebas
if __name__ == '__main__':
    unittest.main()
