from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    args = '<streamname streamname ...>'
    help = 'Fetch a stream and insert new entries into the database'

    def handle(self, *args, **options):
        
        if 'behance' in args:
            from da.lifestream.importers.behance import BehanceImporter
            messages = BehanceImporter().run()
            self.stdout.write('\n'.join(messages) + '\n')