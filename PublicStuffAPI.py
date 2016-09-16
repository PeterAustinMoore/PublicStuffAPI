import requests
import time
class PublicStuff(object):
    def __init__(self, token):
        self.headers = {"Authorization":"Token token=%s" % token}
        return
    def get_requests(self):
        url = self.make_url('/app/requests?limit=500')
        data = []
        r = self.get_request(url)
        data.append(r['entities'])
        while r['properties']['next_page'] != None:
            start = time.time()
            url = self.make_url('/app/requests?limit=500&page=%s' % str(r['properties']['next_page']))
            r = self.get_request(url)
            print("%s took %s seconds to load" % (url, str(time.time() - start)))
            data.append(r['entities'])
        return data
    def make_url(self, path):
        base_url = 'https://api.publicstuff.com'
        return base_url+path
    def get_request(self,url,*args):
        response = requests.get(url, headers=self.headers)
        print("%s responded with %s bytes of information" %(url, str(len(response.content))))
        if response.status_code == 200:
            return response.json()

token = ''
ps = PublicStuff(token=token)
d = ps.get_requests()
print(len(d))