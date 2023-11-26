import logging
import re

from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(module)s %(name)s.%(funcName)s +%(lineno)s: %(levelname)-8s [%(process)d] %(message)s',
                    )
LOG = logging.getLogger(__name__)


def process_html(html):

    soup = BeautifulSoup(html, 'lxml')

    tags = ['p', 'a', 'span']
    pattern = r"(?:(?<=\s)|(?<=^))[a-zA-ZА-Яа-я-]{6}(?=\s|\,|\.|\:)"

    for tag in tags:
        for html_tag in soup.find_all(tag):
            if html_tag.text != '':
                new_text = re.sub(pattern, r'\g<0>™', html_tag.text)
                if new_text != html_tag.text:
                    html_tag.string = html_tag.text.replace(html_tag.text, new_text)

    return soup.prettify().encode('utf-8')

