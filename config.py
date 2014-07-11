#!/bin/python
# Jacob Henson
# https://github.com/cyberphilia


class Site:
	name = ''
	url = ''
	email = ''
	frequency=0 #in minutes
	count=0
	xpath=None

# Create your sites here.
site1 = Site()
site1.name = 'woot'
site1.url = 'http://www.woot.com'
site1.email = 'someperson@emailprovider.com'
site1.frequency = 33


site2 = Site()
site2.name = 'meh'
site2.url = 'http://www.meh.com/'
site2.email = 'someperson@emailprovider.com'
site2.frequency = 47
site2.xpath='h3'


sites_list = [site1,site2]