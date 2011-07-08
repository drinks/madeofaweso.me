from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
class Command(BaseCommand):
    args = '<streamname streamname ...>'
    help = 'Fetch a stream and insert new entries into the database'
    option_list = BaseCommand.option_list + (
        make_option('-p','--pages', dest='pages', default=1, 
                    help='how many pages should we dig back for new content?'),)

    def handle(self, *args, **options):

        if 'behance' in args:
            from lifestream.importers.behance import BehanceImporter
            if 'pages' in options:
                pages = options['pages']
            else:
                pages = 1
            messages = BehanceImporter().run(pages)
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
