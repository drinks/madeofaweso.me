from BeautifulSoup import BeautifulSoup
from dateutil import parser
from lifestream.models import SocialNetwork, BehanceAccount, BehanceField, BehanceImage, BehanceItem

import urllib2
import datetime

class BehanceImporter():
    def __init__(self):
        self.messages = []
        self.accounts = BehanceAccount.objects.filter(active=True)
        try:
            self.network = SocialNetwork.objects.get(name__iexact='behance')
        except SocialNetwork.DoesNotExist:
            print 'You haven\'t created a network with the name "Behance."'
            return None
        if not self.accounts.count():
            print 'You don\'t have any Behance accounts listed.'
            return None

    def run(self, pages):
        for account in self.accounts:
            stream = self.get_stream(baseurl=account.network.resource().rstrip('/'), username=account.username)
            new_ids = [item['resource_id'] for item in stream]
            old_ids = [item.resource_id for
                        item in list(BehanceItem.objects.filter(resource_id__in=new_ids))]
            add_items = filter(lambda x: x['resource_id'] not in old_ids, stream)
            update_items = filter(lambda x: x['resource_id'] not in new_ids, stream)
            for item in add_items:
                try:
                    authors = item['authors']
                    del item['authors']
                    fields = item['fields']
                    del item['fields']
                    item = BehanceItem(**item)
                    item.save()
                    for author in authors:
                        account, created = BehanceAccount.objects.get_or_create(username=author[1].split('/')[-1], 
                                                                                network_id=self.network.id,)
                        if created:
                            account.name=author[0]
                            account.save()
                        item.authors.add(account.id)
                    for field in fields:
                        field, created = BehanceField.objects.get_or_create(field=field[0], remote_url=field[1])
                        item.fields.add(field.id)
                    self.messages.append('Imported item: %s' % item)
                except:
                    self.messages.append('Failed to import item %s' % item.title)
                    continue
        return self.messages

    def get_stream(self, baseurl=None, username=None):
        items = []
        try:
            soup = BeautifulSoup(urllib2.urlopen('/'.join([baseurl, username])).read())
        except (urllib2.HTTPError, ValueError):
            return items

        els = soup('div', {'class':'cover-body'})
        if els:
            for el in els:
                item = {}
                item['remote_url'] = baseurl + (el.findAll('div',{'class':'cover-name'})[0].find('a').get('href') or '/'+username)
                item['resource_id'] = item['remote_url'].split('/')[-1]
                if item['resource_id'] == username:
                    item['resource_id'] = None
                item['thumbnail'] = el.findAll('div',{'class':'cover-img'})[0].find('img').get('src') or ''
                item['title'] = el.findAll('div',{'class':'cover-name'})[0].find('a').getString() or ''
                item['created'] = parser.parse(el.findAll('span',{'class':'coverDate'})[0].getString()) or datetime.datetime.now()
                try:
                    single_author = el.find('div', {'class':'single-owner'}).find('a')
                    item['authors'] = [(single_author.getString(), baseurl + single_author.get('href')),]
                except:
                    try:
                        multiple_authors = el.find('div', {'class':'multiple-owners'}).findAll('a')
                        item['authors'] = [(single_author.getString(), baseurl + single_author.get('href')) for
                                            single_author in multiple_authors]
                    except:
                        pass
                item['fields'] = [(tag.getString(), baseurl + tag.get('href')) for
                            tag in el.find('div', {'class':'cover-field-wrap'}).findAll('a')]
                items.append(item)

        return items

    def get_item(self, url=None):
        item = None
        return item