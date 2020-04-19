import os
import re
import requests

from bs4 import BeautifulSoup
import youtube_dl

USERNAME = 'paulo.menezes@iteris.com.br'
PASSWORD = '271b8e39'

SIGNIN_URL = 'https://cursos.alura.com.br/signin'

HOME_DIR = os.getcwd()

def do_auth(user, pwd):

    post_data = {
        'username': user,
        'password': pwd
    }

    profile_page = sess.post(SIGNIN_URL, post_data)
    
    profile_page_soup = BeautifulSoup(profile_page.text, 'html.parser')

    auth_sign = profile_page_soup.title.text

    if auth_sign:
        if auth_sign.lower().find('dashboard') != -1:
            print('Logado com sucesso!')
        else:
            print('Login não encontrado\nExit...')
            os.sys.exit(0)
    else:
        raise Exception('Falha ao se logar')

    return sess


def http_get(url):
    resp = sess.get(url)
    return resp.text


def move_to_course_directory(title):

    if os.getcwd() != HOME_DIR:
        os.chdir(HOME_DIR)
    try:
        # Cria um diretório com o nome do curso
        os.mkdir(title)
        os.chdir(title)
    except FileExistsError:
        os.chdir(title)
    except:
        print('Could not create subdirectory for the course: {}'.format(title))

sess = do_auth(USERNAME, PASSWORD)