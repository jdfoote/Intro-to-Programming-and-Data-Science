import requests
import re
from auth import *

url = 'https://wiki.communitydata.science/api.php'
old_course_prefix = 'Intro to Programming and Data Science (Spring 2020)'
new_course_prefix = 'Intro to Programming and Data Science (Summer 2020)'
CSRF_TOKEN = None
S = requests.Session()

def get_pages(query = old_course_prefix):
    params = {'action':'query',
    'format':'json',
    'prop':'revisions',
    'list':'search',
    'srsearch': query,
    'srlimit': 500
    }
    r = S.get(url=url, params = params)
    pages = r.json()['query']['search']
    result = {}
    for page in pages:
        if page['ns'] == 0:
            result[page['pageid']] = {'title': page['title']}
    return result


def get_content(pageids):
    '''Assumes that this list is small and that the result will come back in one call.'''
    pageids = '|'.join([str(x) for x in pageids])
    params = {'action':'query',
            'format':'json',
            'prop':'revisions',
            'pageids': pageids,
            'rvprop': 'content'}
    
    r = S.get(url=url, params = params)

    if r.status_code != 200:
        r.raise_for_status()
    return r.json()['query']['pages']


def replace_content(content,
        old_prefix = old_course_prefix,
        new_prefix = new_course_prefix):
    pattern = re.escape(old_prefix)
    return re.sub(pattern, new_prefix, content)


def make_page(title, content):
    if not CSRF_TOKEN:
        login()

    params = {
            'action':'edit',
            'format':'json',
            'title':title,
            'text':content,
            'summary':'Copying content from previous class',
            'token':CSRF_TOKEN
            }
    r = S.post(url, data=params)
    print(r.json())


def login():
    params0 = {
            'action':'query',
            'meta':'tokens',
            'type':'login',
            'format':'json'
            }

    r = S.get(url=url, params = params0)
    LOGIN_TOKEN= r.json()['query']['tokens']['logintoken']

    params1 = {
            'action':'clientlogin',
            'username':uname,
            'password':password,
            'logintoken':LOGIN_TOKEN,
            'format':'json',
            'loginreturnurl':'http://127.0.0.1:5000/'
            }
    r = S.post(url, data=params1)
    if r.json()['clientlogin']['status'] != 'PASS':
        r.raise_for_status()

    # Get CSRF token
    params2 = {
            'action':'query',
            'meta':'tokens',
            'format':'json'
            }
    r = S.get(url=url, params=params2)
    global CSRF_TOKEN
    CSRF_TOKEN = r.json()['query']['tokens']['csrftoken']




pages = get_pages()
print(len(pages))

ids = pages.keys()

content_dict = get_content(ids)

new_pages = []
for curr_page, value in content_dict.items():
    curr_page_id = int(curr_page)
    curr_content = value['revisions'][0]['*']
    curr_title = pages[curr_page_id]['title']

    new_title = replace_content(curr_title)
    new_content = replace_content(curr_content)

    user_input = input('Copy {} to {}? [y]/n?'.format(curr_title, new_title))
    copy_bool = user_input not in ['N','n', 'no','No']
    if copy_bool:
        make_page(new_title, new_content)

