"""
    ecriture d'une commande django pour attendre que la bd soit demmarer et disponible 
"""

from typing import Any
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """ les methodes dela commande attendre la bd """

    def handle(self, *args: Any, **options: Any):
        pass

