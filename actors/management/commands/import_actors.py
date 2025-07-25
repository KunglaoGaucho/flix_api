from django.core.management.base import BaseCommand
from datetime import datetime
import csv
from actors.models import Actors


# Classe para executar o comando.
class Command(BaseCommand):

    # Reescrevendo a função add_arguments de BaseCommand e passando os argumentos necessários
    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo CSV com atores'
        )

    # Capturando os dados que precisamos, que esta no arquivo "actors.csv"
    def handle(self, *args, **options):
        file_name = options['file_name']

        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                birthday = datetime.strptime(row['birthday'], '%Y-%m-%d').date()
                nationality = row['nationality']

                self.stdout.write(self.style.NOTICE(name))

                Actors.objects.create(
                    name=name,
                    birthday=birthday,
                    nationality=nationality,
                )

        self.stdout.write(self.style.SUCCESS('ATORES IMPORTADOS COM SUCESSO'))  # É basicamente um print porém mais bonitinho
