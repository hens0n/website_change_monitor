#!/bin/python
# Jacob Henson
# https://github.com/cyberphilia

# Standard Modules
import difflib               
import urllib2
import sys
import os
import os.path
import re
from httplib import HTTPConnection, socket
# Third Party Modules
from bs4 import BeautifulSoup
# My modules
from config import Site


def compare_pevious_and_current(site):
    print site.name
    previous = read_file(('%s.html' % site.name))
    current = get_html(site.url)

    if (previous):
        if(site.xpath):
            soup = BeautifulSoup(current)
            soup_xpath = soup.findAll(site.xpath)
            temp = ''
            for result in soup_xpath:
                temp+=result.get_text()
            # print temp  
            if(diff_text(previous,temp)):
                write_file(('%s.html' % site.name), temp)
                return True

        else:            
            if(diff_text(previous,current)):
                write_file(('%s.html' % site.name), current)
                return True
            else:
                print 'diff not found, do nothing'

    else:
        # first check
        write_file(('%s.html' % site.name), current)

    return False



def diff_text(text1,text2):
    diff_generator = difflib.unified_diff(text1, text2)
    for differences in diff_generator:
        return True
    return False

def get_html(url):
    try:
        headers = { 'User-Agent' : 'webmon/1.0' }
        req = urllib2.Request(url, None, headers)
        html = urllib2.urlopen(req).read()
        return html
    except urllib2.URLError as reason :
        error("URLError : %s" % (reason,), 2)        
    except  ValueError :
        error("Invalid URL : %s" % current_url, 2)
        
def validate_url(url) :
    # django regex for url validation
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if re.search(regex, url) == None :
        return 0
    else :
        return 1
def read_file(filename):
    if(os.path.isfile(filename)):
        file_object = open(filename,'r')
        text = file_object.read()
        file_object.close()
        return text
    else:
        return None
def write_file(filename,text):
    file_object = open(filename,'w')
    file_object.write(text)
    file_object.close()
