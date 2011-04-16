from BeautifulSoup import BeautifulSoup
from dateutil import parser
from da.lifestream.models import BehanceAuth, BehanceItem, BehanceAuthor, BehanceTag

import urllib2
import datetime

class BehanceImporter():
    def __init__(self):
        self.auths = BehanceAuth.objects.all()

    def run(self):
        messages = []
        for auth in self.auths:
            stream = self.get_stream(baseurl=auth.base_url.rstrip('/'), username=auth.username)
            new_ids = [item['resource_id'] for item in stream]
            old_ids = [item.resource_id for 
                        item in list(BehanceItem.objects.filter(resource_id__in=new_ids))]
            items = filter(lambda x: x['resource_id'] not in old_ids, stream)
            for item in items:
                # try:
                authors = item['authors']
                del item['authors']
                btags = item['tags']
                item['tags'] = ','.join([tag[0] for tag in btags])
                # item['slug'] = item['title']
                item = BehanceItem(**item)
                item.save()
                for author in authors:
                    author, created = BehanceAuthor.objects.get_or_create(name=author[0], remote_url=author[1])
                    item.authors.add(author.id)
                for tag in btags:
                    tag, created = BehanceTag.objects.get_or_create(tag=tag[0], remote_url=tag[1])
                    item.behance_tags.add(tag.id)
                messages.append('Imported item: %s' % item)
                # except:
                    # messages.append('Failed to import item %s' % item.get('title', ''))
                    # continue
        return messages
        
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
                item['tags'] = [(tag.getString(), baseurl + tag.get('href')) for
                            tag in el.find('div', {'class':'cover-field-wrap'}).findAll('a')]
                items.append(item)

        return items