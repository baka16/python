import requests
from bs4 import BeautifulSoup as bs


def get_login_token(raw_resp):
    soup = bs(raw_resp.text, 'lxml')
    token = [n['value'] for n in soup.find_all('input')
             if n['name'] == 'wpLoginToken']
    return token[0]

payload = {
    'wpName': 'my_username',
    'wpPassword': 'my_password',
    'wpLoginAttempt': 'Log in',
    #'wpLoginToken': '',
    }

with requests.session() as s:
    resp = s.get('http://en.wikipedia.org/w/index.php?title=Special:UserLogin')
    payload['wpLoginToken'] = get_login_token(resp)

    response_post = s.post('http://en.wikipedia.org/w/index.php?title=Special:UserLogin&action=submitlogin&type=login',
                           data=payload)
    response = s.get('http://en.wikipedia.org/wiki/Special:Watchlist')
    
    
    
 ##########################################################################################
 
 
 import requests
from bs4 import BeautifulSoup as bs


def get_session_id(raw_resp):
    soup = bs(raw_resp.text, 'lxml')
    token = soup.find_all('input', {'name':'survey_session_id'})[0]['value']
    return token

payload = {
    'f213054909': 'o213118718',  # 21st checkbox
    'f213054910': 'Ronald',  # first input-field
    'f213054911': 'ronaldG54@gmail.com',
    }

url = r'https://app.e2ma.net/app2/survey/39047/213008231/f2e46b57c8/?v=a'

with requests.session() as s:
    resp = s.get(url)
    payload['survey_session_id'] = get_session_id(resp)
    response_post = s.post(url, data=payload)
    print response_post.text
    
    
##########################################################################################



