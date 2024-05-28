""" 
    Test des commande
"""

from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2Erroor


from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.Check')
class CommandTests(SimpleTestCase):
    """ class de test des commandes """

    def test_wait_for_db_ready(self):
        """ Methorde de test """
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(database=['default'])

    # Utilisation du décorateur @patch pour remplacer la fonction time.sleep par une version simulée dans le contexte du test
    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for database when getting OperationalError."""
        
        # Configuration du comportement simulé de la fonction check lors de son appel
        patched_check.side_effect = [Psycopg2OpError] * 2 + [OperationalError] * 3 + [True]
