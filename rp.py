import requests
import random
from datetime import datetime
import time
import logmanager
import logging

logmanager.get_configured_logger()

def __get_random_url():
    urls = [
        'https://picsum.photos/150/220',
        'https://api.lorem.space/image/movie?w=150&h=220',
        'https://api.lorem.space/image/game?w=150&h=220',
        'https://api.lorem.space/image/album?w=150&h=150',
        'https://api.lorem.space/image/book?w=150&h=220',
        'https://api.lorem.space/image/pizza?w=150&h=150',
        'https://api.lorem.space/image/burger?w=150&h=150'
    ]
    return random.choice(urls)

def __get_filename():
    now = datetime.now()
    nowstr = now.strftime('%Y%m%d%H%M%S%f')
    return f'{nowstr}.jpg'


def __dl_picture():
    start_time = datetime.now()
    url = __get_random_url()
    
    filename = __get_filename()
    logging.debug(f'downloading url: {url} into {filename}')
    response = requests.get(url, stream=True)   #download the data as stream

    try:
        if response.status_code == 200:
            with open(filename, 'wb') as fh:
                for chunk in response.iter_content(512):    #read in chunks of 512 bytes
                    fh.write(chunk)
    except Exception as e:
        logging.exception('error downloading resource')

    end_time = datetime.now()
    elapsed = end_time - start_time
    logging.debug(f'elapsed: {elapsed}')

def run():
    for i in range(10):
        __dl_picture()



if __name__ == '__main__':
    run()