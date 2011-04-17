from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    args = '<streamname streamname ...>'
    help = 'Fetch a stream and insert new entries into the database'

    def handle(self, *args, **options):

        if 'behance' in args:
            from moa.lifestream.importers.behance import BehanceImporter
            messages = BehanceImporter().run()
            self.stdout.write('\n'.join(messages) + '\n')

        if 'dribbble' in args:
            pass

        if 'flickr' in args:
            pass

        if 'forrst' in args:
            pass

        if 'instagram' in args:
            pass

        if 'twitter' in args:
            pass
